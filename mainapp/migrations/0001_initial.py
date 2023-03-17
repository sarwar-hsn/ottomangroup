# Generated by Django 4.1.1 on 2023-03-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('home', 'home'), ('about', 'about'), ('contact', 'contact'), ('services_home', 'services_home'), ('real_estate', 'real_estate'), ('citizenship', 'citizenship'), ('study', 'study'), ('export_import', 'export_import'), ('hajj_umrah', 'hajj_umrah'), ('tourism', 'tourism'), ('service_solutions', 'service_solutions'), ('property_home', 'property_home'), ('blog_home', 'blog_home'), ('blog_category', 'blog_category'), ('blog_hashtag', 'blog_hashtag'), ('apply_education', 'apply_education'), ('book_consultancy', 'book_consultancy')], max_length=40, unique=True)),
                ('seo_title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, default='The Ottoman Group, tog,Turkiye, Real Estate, Turkish Citizenship study in turkey, Turkey,Tourism,turkish tourism,health tourism', null=True)),
                ('page_url', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('locale', models.CharField(default='en_US', max_length=10)),
                ('use_og', models.BooleanField(default=False)),
                ('use_twitter', models.BooleanField(default=False)),
                ('use_facebook', models.BooleanField(default=False)),
                ('use_schemaorg', models.BooleanField(default=False)),
            ],
        ),
    ]
