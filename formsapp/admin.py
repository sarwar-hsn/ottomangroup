from django.contrib import admin
from .models import Consultancy, Education, Contact
# Register your models here.
admin.site.register(Consultancy)
admin.site.register(Education)
admin.site.register(Contact)