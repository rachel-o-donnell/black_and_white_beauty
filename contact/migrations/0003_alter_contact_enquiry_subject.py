# Generated by Django 3.2 on 2023-05-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='enquiry_subject',
            field=models.CharField(choices=[(None, 'Pick a Subject'), ('Commissions', 'Commissions'), ('Complaint', 'Complaint'), ('Orders', 'Orders'), ('Returns', 'Returns'), ('Other', 'Other')], max_length=20),
        ),
    ]