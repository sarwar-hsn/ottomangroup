# Generated by Django 4.1.1 on 2023-03-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0005_property_featured_property_last_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='amenities',
            field=models.CharField(blank=True, choices=[('pool', 'Pool'), ('garage', 'Garage'), ('fireplace', 'Fireplace'), ('central air', 'Central Air Conditioning')], max_length=20, null=True),
        ),
    ]
