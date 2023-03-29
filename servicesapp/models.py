from django.db import models
import os
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from sorl.thumbnail import ImageField, delete  
from django_cleanup.signals import cleanup_pre_delete
from django.forms.models import model_to_dict
from meta.models import ModelMeta

# Create your models here.
from django.db import models


def property_thumbnail_path(instance,filename,*args, **kwargs):
    datetime = instance.created_at
    year = datetime.strftime('%Y')
    month = datetime.strftime('%b')
    base, ext = os.path.splitext(filename)
    return f"properties/{year}/{month}/{instance.slug}/thumbnail/{base}_big{ext}"


class Property(ModelMeta,models.Model):
    PROPERTY_TYPES = (
        ('townhouse', 'Townhouse'),
        ('condo', 'Condominium'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
    )

    AMENITIES = (
        ('pool', 'Pool'),
        ('garage', 'Garage'),
        ('fireplace', 'Fireplace'),
        ('central air', 'Central Air Conditioning'),
    )
    seo_title = models.CharField(max_length=200,blank=True,null=True)
    seo_description = models.TextField(blank=True,null=True)
    seo_keywords = models.TextField(blank=True,null=True)
    seo_imagelink = models.URLField(null=True,blank=True)
    #regular properties
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True,max_length=250)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.IntegerField()
    bedrooms = models.CharField(max_length=20)
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    floor_location =models.IntegerField(blank=True,null=True)
    no_of_floors =models.IntegerField(blank=True,null=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=200,blank=True,null=True)
    age = models.IntegerField(blank=True, null=True)
    amenities = models.CharField(max_length=20, choices=AMENITIES, blank=True,null=True)
    thumbnail = ImageField(upload_to=property_thumbnail_path)
    featured = models.BooleanField(default=False)
    
    
    def get_model_dictionay(self):
        dic = {
            'posted on':self.created_at,
            'property type':self.property_type,
            'bedrooms':self.bedrooms,
            'bathrooms':self.bathrooms,
            'sqft':str(self.sqft)+" sqft",
            'no. of floors': self.no_of_floors,
            'city': self.city,
            'state':self.state,
            'address':self.address,
            'building age':self.age,
            'amenities':self.amenities,
        }
        return dic
    
    
    #seo meta
    #expects array of string
    def get_seo_keywords(self):
        if self.seo_keywords:
            return str.split(self.seo_keywords,sep=",")
        else:
            return None

    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return self.title
    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description;
        return self.description;
    def get_seo_image(self):
        if self.seo_imagelink:
            return self.seo_imagelink;
        else:
            return self.thumbnail.url;
                    
    _metadata = {
        'use_og':True,
        'use_twitter':True,
        'use_facebook':True,
        'use_schemaorg':True,
        'title':'get_seo_title',
        'description':'get_seo_description',
        'keywords':'get_seo_keywords',
        'image': 'get_seo_image',
        'url':'get_absolute_url',
        'locale':'en_US',
    }
    #end se0

    class Meta:
        ordering =['-created_at']
        verbose_name ='property'
        verbose_name_plural='properties'

    def is_uniqueslug(self):
        try:
            property = Property.objects.get(slug=slug)
            return property #if category is present then we return the category
        except: #if we encounter any error then we will return the error
            return None
    def clean(self):
        if self.slug is None:
            self.slug = slugify(self.title)
        post = self.is_uniqueslug()
        if post is None: #that mean the slug is unique, no category using this slug
            return
        else: #if the category is found that means the slug is not unique
            raise ValidationError(f"slug: {self.slug} is not unique. change it manually")

    def save(self, *args, **kwargs):
        super(Property,self).save(*args, **kwargs)  # Call the "real" save() method.
    def get_absolute_url(self):
        return reverse("servicesapp:servicesapp_property_details", kwargs={"prop_slug": self.slug})
    
    def get_thumbnail(self):
        return self.thumbnail

    

    def __str__(self):
        return self.title
    

def property_image_path(instance,filename,*args, **kwargs):
    datetime = instance.property.created_at
    year = datetime.strftime('%Y')
    month = datetime.strftime('%b')
    base, ext = os.path.splitext(filename)
    return f"properties/{year}/{month}/{instance.property.slug}/images/{base}_big{ext}"


def validate_file_size(value):
    filesize= value.size
    if filesize > 204800:
        raise ValidationError("You cannot upload file more than 200kb")
    else:
        return value
        
class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_image_path,validators=[validate_file_size])
    def __str__(self):
        return f"{self.property.slug}_{self.pk}"
    
    def get_gallery_images(property):
        if property is None:
            return None
        else:
            images = []
            images.append(property.thumbnail)
            queryset =  PropertyImages.objects.filter(property=property)
            for q in queryset:
                images.append(q.image)
            return images

def sorl_delete(**kwargs):
    delete(kwargs['file'])
cleanup_pre_delete.connect(sorl_delete)