from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.content = validated_data.get('content')
        instance.created_at = validated_data.get('created_at')
        instance.author = validated_data.get('author')
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        instance = Comment.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content')
        instance.created_at = validated_data.get('created_at')
        instance.post = validated_data.get('post')
        instance.author = validated_data.get('author')
        instance.save()
        return instance
