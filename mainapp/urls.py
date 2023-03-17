from django.urls import path
from . import views


app_name = 'mainapp'


urlpatterns = [
    path('about/',views.about,name="mainapp_about"),
    path('contact/',views.contact,name="mainapp_contact"),
    path('',views.index,name="mainapp_index"),
]
