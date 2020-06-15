from rest_framework import serializers
from .models import PostArticle

class PostArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostArticle
        fields = {
            'title', 'description'
        }