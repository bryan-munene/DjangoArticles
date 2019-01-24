from rest_framework import serializers
from .models import Articles

class ArticlesSerializers(serializers.ModelSerializer):
    """This class maps model instance onto it's coresponding JSON format."""

    class Meta:
        """This meta class maps the model fields to coresponding instance fields"""
        model = Articles
        fields = ('id', 'name', 'text', 'author', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')