from pathlib import Path
from urllib.parse import urlparse
from django.db import models
from colorthief import ColorThief
import requests
import os

BASE_DIR = Path(__file__).resolve().parent.parent
    
class Photo(models.Model):
    title = models.CharField(max_length=200)
    albumId = models.IntegerField()
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(
                              height_field='height',
                              width_field='width',
                              blank=True,
                              null=True)
    url = models.URLField(max_length=200, blank=True)
    dominant_color = models.CharField(max_length=200, blank=True, null=True)
        
    def get_remote_image(self):
        img_data = requests.get(self.url+'.jpg')
        filename = os.path.basename(urlparse(self.url).path)
        with open('media/'+filename+'.jpg', 'wb') as handler:
            handler.write(img_data.content)
        self.image = os.path.join(BASE_DIR, 'media/'+filename+'.jpg')
        self.save()
        return self.image

    def get_dominant_color(self):
        color_thief = ColorThief(self.image.open())
        dominant_color = color_thief.get_color(quality=1)
        dominant_color_hex = '#%02x%02x%02x' % dominant_color
        self.dominant_color = dominant_color_hex
        self.save()
        return self.dominant_color