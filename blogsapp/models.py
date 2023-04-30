from django.db import models
from django.utils.text import slugify
import os
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from mainapp.utils.helpers import my_reverse
from sorl.thumbnail import ImageField, delete  
from django_cleanup.signals import cleanup_pre_delete
from meta.models import ModelMeta
from tinymce.models import HTMLField 

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    joined = models.DateTimeField( auto_now_add=True)
    bio = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.email
    
#tag
class Tag(models.Model):
    name = models.CharField(max_length=30)
    view_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blogsapp:blogsapp_hashtag',kwargs={'tag':self.name})
    
#category
class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    view_count = models.PositiveIntegerField(default=0)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "category"
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogsapp:blogsapp_category',kwargs={'name':self.name})



def blog_thumbnail_path(instance,filename,*args, **kwargs):
    datetime = instance.created_at
    year = datetime.strftime('%Y')
    month = datetime.strftime('%b')
    base, ext = os.path.splitext(filename)
    return f"blogs/{year}/{month}/{instance.slug}/thumbnail/{base}{ext}"

class Blog(ModelMeta,models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    post_status =(
        (DRAFT,DRAFT),
        (PUBLISHED,PUBLISHED)
    )
    seo_title = models.CharField(max_length=200,blank=True,null=True)
    seo_description = models.TextField(blank=True,null=True)
    seo_keywords = models.TextField(blank=True,null=True)
    seo_imagelink = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True,max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL)
    thumbnail = ImageField(upload_to=blog_thumbnail_path,)
    thumbnail_alt = models.CharField(max_length=100)
    overview = models.TextField()
    tags = models.ManyToManyField(Tag,blank=True)
    content = HTMLField()
    status = models.CharField(max_length=20,default=DRAFT,choices=post_status)
    rating = models.IntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    
    #seo meta
    #expects array of string
    def get_seo_keywords(self):
        if self.seo_keywords:
            return str.split(self.seo_keywords,sep=",")
        else:
            keywords = []
            for tag in self.tags.all():
                keywords.append(tag.name)
        return keywords
    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return self.title
    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description;
        return self.overview;
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
    
    def is_uniqueslug(self):
        try:
            blog = Blog.objects.get(slug=slug)
            return blog #if category is present then we return the category
        except: #if we encounter any error then we will return the error
            return None

    def clean(self):
        if self.slug is None:
            self.slug = slugify(self.title)
        blog = self.is_uniqueslug()
        if blog is None: #that mean the slug is unique, no category using this slug
            return
        else: #if the category is found that means the slug is not unique
            raise ValidationError(f"slug: {self.slug} is not unique. change it manually")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blogsapp:blogsapp_blog", kwargs={"blog_slug": self.slug})

    def get_thumbnail(self):
        return self.thumbnail



def blog_image_path(instance,filename,*args, **kwargs):
    datetime = instance.blog.created_at
    year = datetime.strftime('%Y')
    month = datetime.strftime('%b')
    base, ext = os.path.splitext(filename)
    return f"blogs/{year}/{month}/{instance.blog.slug}/images/{base}{ext}"

def validate_file_size(value):
    filesize= value.size
    if filesize > 3145728:
        raise ValidationError("You cannot upload file more than 300kb")
    else:
        return value
        
class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=blog_image_path,validators=[validate_file_size])
    def __str__(self):
        return f"{self.blog.slug}_{self.pk}"

def sorl_delete(**kwargs):
    delete(kwargs['file'])
cleanup_pre_delete.connect(sorl_delete)

