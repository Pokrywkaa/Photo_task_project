from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from photo_app.models import Photo
import json

class APITestAll(APITestCase):
    def test_get_photos_list(self):
        list_url = reverse('photos:photos_list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_photo(self):
        data = {
            "albumId": 1,
            "title": "accusamus beatae ad facilis cum similique qui sunt",
            "url": "https://via.placeholder.com/600/92c952"
        }
        list_url = reverse('photos:photos_list')
        response = self.client.post(list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

class APITestSingle(APITestCase):
    def setUp(self):
            self.photo1 = Photo.objects.create(
                albumId=1, url="https://via.placeholder.com/600/92c952", title='test'
            )
            self.valid_payload = {
                "albumId": 1,
                "title": "test-update",
                "url": "https://via.placeholder.com/600/92c952"
            }
            self.invalid_payload = {
                "albumId": "",
                "title": "test-update",
                "url": "https://via.placeholder.com/600/92c952"
            }
            
    def test_delete_photo(self):
        list_url = reverse('photos:photo_detail', kwargs={"pk":self.photo1.pk})
        response = self.client.delete(list_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_valid_update_photo(self):
        list_url = reverse('photos:photo_detail', kwargs={'pk':self.photo1.pk})
        response = self.client.put(list_url,
                                    data=json.dumps(self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_invalid_update_photo(self):
        list_url = reverse('photos:photo_detail', kwargs={'pk':self.photo1.pk})
        response = self.client.put(list_url,
                                    data=json.dumps(self.invalid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        