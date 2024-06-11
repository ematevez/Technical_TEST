from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Post
        fields = ['email', 'file']