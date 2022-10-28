# Photo_task_project
Migrate data to database:
```
docker-compose run web python manage.py migrate
```
Get photos from external API:
```
docker-compose run web python manage.py runscript get_photos_from_api
```
Get photos from json file (path=/scripts/test.json):
```
docker-compose run web python manage.py runscript get_photos_from_json_file
```
Create superuser:
```
docker-compose run web python manage.py createsuperuser
```
Run django app with postgresql:
```
docker-compose up
```
