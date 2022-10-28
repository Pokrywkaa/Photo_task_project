# Generated by Django 4.1.2 on 2022-10-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0003_photo_dominant_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, height_field='height', upload_to='photos/%Y/%m/%d', width_field='width'),
        ),
    ]