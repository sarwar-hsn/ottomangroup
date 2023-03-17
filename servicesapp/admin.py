from django.contrib import admin
from .models import Property,PropertyImages
# Register your models here.

class PropertyImagesAdmin(admin.StackedInline):
    model = PropertyImages

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImagesAdmin]

admin.site.register(Property,PropertyAdmin)