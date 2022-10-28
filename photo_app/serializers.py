from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='get_remote_image',required=False)
    dominant_color = serializers.CharField(source='get_dominant_color',required=False)
    class Meta:
        model = Photo
        fields = '__all__'

