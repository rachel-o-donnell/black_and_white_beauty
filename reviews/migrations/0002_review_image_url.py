# Generated by Django 3.2 on 2023-05-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
