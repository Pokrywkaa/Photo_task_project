from photo_app.models import Photo
import requests

def run():
    r = requests.get('https://jsonplaceholder.typicode.com/photos')
    r_status = r.status_code
    if r_status == 200:
        data = r.json()
        for item in data:
            photo = Photo(
                title = item['title'],
                albumId = item['albumId'],
                url = item['url'],
            )
            photo.get_remote_image()
            photo.get_dominant_color()
            photo.save()
        
