from rest_framework import serializers
from .models import PasswordCollection, WebSitePassword, WifiPassword, WebSiteBookmark


BLACK_LISTED_PASSWORDS = ['qazwsxedcv', 'password', 'qwerty']
BLACK_LISTED_URLS = ['a.kz', 'a.ba']
BLACK_LISTED_CHARS = ['*', '?', '|', '>', '<']


class BaseCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordCollection

    def validate(self, attrs):
        if attrs['name']:
            for ch in attrs['name']:
                if ch in BLACK_LISTED_CHARS:
                    raise serializers.ValidationError('incorrect name')
        return attrs


class PasswordCollectionSerializer(BaseCollectionSerializer):
    class Meta:
        model = PasswordCollection
        fields = ('name',)


class PasswordCollectionsSerializer(BaseCollectionSerializer):
    class Meta:
        model = PasswordCollection
        fields = '__all__'


class PasswordSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    collection = PasswordCollectionsSerializer()


class WebSitePasswordSerializer(PasswordSerializer):
    website = serializers.CharField(max_length=255)
    login = serializers.CharField(max_length=100)

    def create(self, validated_data):
        validated_data['collection'] = PasswordCollection.objects.get(name=validated_data['collection']['name'])
        return WebSitePassword.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs['password'] in BLACK_LISTED_PASSWORDS:
            raise serializers.ValidationError('too common password')
        return attrs


class WifiPasswordSerializer(PasswordSerializer):
    wifi_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        validated_data['collection'] = PasswordCollection.objects.get(name=validated_data['collection']['name'])
        return WifiPassword.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs['password'] in BLACK_LISTED_PASSWORDS:
            raise serializers.ValidationError('too common password')
        return attrs


class BookmarkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class WebSiteBookmarkSerializer(BookmarkSerializer):
    description = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    website_password = WebSitePasswordSerializer()

    def create(self, validated_data):
        website_password = WebSitePassword.objects.filter(name=validated_data['website_password']['name'])[0]
        validated_data['website_password'] = website_password
        return WebSiteBookmark.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs['url'] in BLACK_LISTED_URLS:
            raise serializers.ValidationError('web site is not supported')
        return attrs
