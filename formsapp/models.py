from django.db import models
from django.utils import timezone


# Create your models here.

class Education(models.Model):
    edu_status = [
        ('hsc','HSC'),
        ('undergraduate','Bachelor Degree'),
        ('post-graduate','Masters Degree'),
        ('other','Other')
    ]
    university_type =[
        ('private-university','public university'),
        ('public-university','public university'),
        ('medical-university','medical university'),
        ('language-institution','language institution'),
    ]
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    date_of_birth = models.DateField(default=timezone.datetime(2000,1,1))
    country = models.CharField(max_length=30,default="Bangladesh")
    university_preference = models.CharField(max_length=30,choices=university_type)
    present_education_status = models.CharField(choices=edu_status, max_length=50)
    applying_for = models.CharField(choices=edu_status,max_length=50)
    preferred_department = models.CharField(max_length=100)
    message = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = "education-apply"
        verbose_name_plural = 'education-applies'
        ordering = ['-created']

    def __str__(self):
        return f"{self.full_name} {self.created}"
    
    def get_property_values(self):
        values = ""
        values+="created       : "+str(self.created)+"\n"
        values+="full name     : "+str(self.full_name)+"\n"
        values+="email         : "+str(self.email)+"\n"
        values+="whatsapp      : "+str(self.whatsapp)+"\n"
        values+="date_of_birth : "+str(self.date_of_birth)+"\n"
        values+="country       : "+str(self.country)+"\n"
        values+="varsity pref  : "+str(self.university_preference)+"\n"
        values+="edu status    : "+str(self.present_education_status)+"\n"
        values+="edu status    : "+str(self.applying_for)+"\n"
        values+="pref dept     : "+str(self.preferred_department)+"\n"
        values+="message       : "+str(self.message)+"\n"
        return values

class Consultancy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    message = models.TextField(blank=True,null=True)
    spam = models.BooleanField(default=False)

    class Meta:
        verbose_name = "consultancy"
        verbose_name_plural = 'consultancies'
        ordering = ['-created']

    def __str__(self):
        return f"{self.full_name} {self.created}"

    def get_property_values(self):
        values = ""
        values+="created    : "+str(self.created)+"\n"
        values+="full name  : "+str(self.full_name)+"\n"
        values+="email      : "+str(self.email)+"\n"
        values+="whatsapp   : "+str(self.whatsapp)+"\n"
        values+="country    : "+str(self.country)+"\n"
        values+="scheduled  : "+str(self.date)+" - "+str(self.time.hour)+":"+str(self.time.min)+"\n"
        values+="message    : "+str(self.message)+"\n"
        return values

class Contact(models.Model):
    service_choice =[
        ('education','education'),
        ('real-estate','real-estate'),
        ('citizenship&residence','cititzenship or residence permit'),
        ('tourism','tourism'),
        ('export-import','export-import'),
        ('service-solution','service solution'),
        ('hajj-umrah','hajj-umrah'),
        ('other','other')
    ]
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    department = models.CharField(max_length=30,choices=service_choice)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.full_name} {self.created}"

    def get_property_values(self):
        values = ""
        values+="created    : "+str(self.created)+"\n"
        values+="full name  : "+str(self.full_name)+"\n"
        values+="email      : "+str(self.email)+"\n"
        values+="whatsapp   : "+str(self.whatsapp)+"\n"
        values+="department : "+str(self.department)+"\n"
        values+="message    : "+str(self.message)+"\n"
        return values
    


    
