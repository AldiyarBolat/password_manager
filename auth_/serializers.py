from rest_framework import serializers

from .models import Profile


COUNTRIES = ['KZ', 'RU', 'US']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate(self, attrs):
        if attrs['country'] and attrs['country']  not in COUNTRIES:
            raise serializers.ValidationError('incorrect country')
        return attrs
