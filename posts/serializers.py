from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'likes',
            'owner',
            'thumbnail',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')

    def get_thumbnail(self, obj):
        return obj.get_thumbnail_url()


class PostPhotoSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    photo = serializers.ImageField(write_only=True)

    class Meta:
        model = Post
        fields = ['photo', 'thumbnail']
        read_fields_only = ['thumbnail']

    def get_thumbnail(self, obj):
        return obj.get_thumbnail_url()
