from django.db import models

# Create your models here.




class seo(models.Model):
    DEFAULT_KEYWORDS = "The Ottoman Group, tog,Turkiye, Real Estate, Turkish Citizenship study in turkey, Turkey,Tourism,turkish tourism,health tourism"
    pages = [
        ('home','home'),
        ('about','about'),
        ('contact','contact'),
        ('services_home','services_home'),
        ('real_estate','real_estate'),
        ('citizenship','citizenship'),
        ('study','study'),
        ('study_packages','study_packages'),
        ('export_import','export_import'),
        ('hajj_umrah','hajj_umrah'),
        ('tourism','tourism'),
        ('service_solutions','service_solutions'),
        ('property_home','property_home'),
        ('blog_home','blog_home'),
        ('blog_category','blog_category'),
        ('blog_hashtag','blog_hashtag'),
        ('apply_education','apply_education'),
        ('book_consultancy','book_consultancy'),
    ] 
    page = models.CharField(max_length=40,choices=pages,unique=True)
    seo_title = models.CharField(max_length=100,)
    description = models.TextField(blank=True,null=True)
    keywords = models.TextField(blank=True,null=True,default=DEFAULT_KEYWORDS)
    page_url = models.URLField(max_length=200,blank=True,null=True)
    image_url = models.URLField(blank=True,null=True)
    locale = models.CharField(max_length=10,default='en_US')
    use_og = models.BooleanField(default=False)
    use_twitter = models.BooleanField(default=False)
    use_facebook = models.BooleanField(default=False)
    use_schemaorg = models.BooleanField(default=False)

    def string_to_array(self):
        return self.keywords.split(sep=",")

    def __str__(self):
        return self.page
    
