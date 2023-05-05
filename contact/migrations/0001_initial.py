# Generated by Django 3.2 on 2023-05-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('enquiry_subject', models.CharField(choices=[('Commissions', 'Commissions'), ('Complaint', 'Complaint'), ('Orders', 'Orders'), ('Returns', 'Returns'), ('Other', 'Other')], max_length=20)),
                ('body', models.TextField(max_length=1000)),
                ('dimensions', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('order_number', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
