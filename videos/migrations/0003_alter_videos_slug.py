# Generated by Django 5.0.6 on 2024-05-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videos_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
