from django.urls import path
from . import views

app_name = 'formsapp'


urlpatterns = [
    path('apply-study/',views.edu_apply,name="formsapp_apply_study"),
    path('book-an-hour/',views.book_consultancy,name="formsapp_book_consultancy"),
    path('contact/',views.contact,name="formsapp_contact"),
]
