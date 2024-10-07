from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        instance = Profile.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user')
        instance.bio = validated_data.get('bio')
        instance.picture = validated_data.get('picture')
        instance.save()
        return instance


class FollowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Follow
        fields = '__all__'

    def create(self, validated_data):
        instance = Follow.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user')
        instance.follower = validated_data.get('follower')
        instance.following = validated_data.get('following')
        instance.save()
        return instance
