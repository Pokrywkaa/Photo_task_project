# Generated by Django 4.1.2 on 2022-10-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='width',
            field=models.IntegerField(blank=True),
        ),
    ]
