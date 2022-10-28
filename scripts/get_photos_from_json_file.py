from photo_app.models import Photo
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent

def run():
    f = open(os.path.join(BASE_DIR, 'test.json'))
    data = json.load(f)
    for item in data:
        photo = Photo(
            title = item['title'],
            albumId = item['albumId'],
            url = item['url'],
        )
        photo.get_remote_image()
        photo.get_dominant_color()
        photo.save()