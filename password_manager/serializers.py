from rest_framework import serializers
from .models import PasswordCollection, WebSitePassword, WifiPassword, WebSiteBookmark


class BaseCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordCollection


class PasswordCollectionSerializer(BaseCollectionSerializer):
    class Meta:
        fields = ('name',)


class PasswordCollectionsSerializer(BaseCollectionSerializer):
    class Meta:
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


class WifiPasswordSerializer(PasswordSerializer):
    wifi_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        validated_data['collection'] = PasswordCollection.objects.get(name=validated_data['collection']['name'])
        return WifiPassword.objects.create(**validated_data)


class BookmarkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class WebSiteBookmarkSerializer(BookmarkSerializer):
    description = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    website_password = WebSitePasswordSerializer()

    def create(self, validated_data):
        website_password = WebSitePassword.objects.get(name=validated_data['website_password']['name'])
        validated_data['website_password'] = website_password
        return WebSiteBookmark.objects.create(**validated_data)
