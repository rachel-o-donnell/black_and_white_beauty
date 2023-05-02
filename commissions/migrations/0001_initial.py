# Generated by Django 3.2 on 2023-05-02 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=254)),
                ('brief', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(max_length=1024)),
                ('dimensions', models.CharField(max_length=250)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.category')),
            ],
        ),
    ]
