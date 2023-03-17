# Generated by Django 4.1.1 on 2023-03-13 23:33

from django.db import migrations, models
import servicesapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0003_alter_property_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(upload_to=servicesapp.models.property_image_path, validators=[servicesapp.models.validate_file_size]),
        ),
    ]
