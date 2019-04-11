from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Presentation, Creator 


class CreatorSerializer(ModelSerializer):
    class Meta:
        model = Creator
        fields = [
            'name',
            'profileUrl'
        ]

class PresentationSerializer(ModelSerializer):
    #author= CreatorSerializer
    author = CreatorSerializer( read_only=True)
    id = serializers.CharField(source='ident')
    
    class Meta:
        model = Presentation
        fields = [
            'id',
            'title',
            'thumbnail',
            'author',
            'createdAt',
        ]

