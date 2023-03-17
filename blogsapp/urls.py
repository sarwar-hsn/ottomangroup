from django.urls import path
from . import views

app_name = 'blogsapp'

urlpatterns = [
    path('category/<str:name>',views.category,name="blogsapp_category"),
    path('hashtag/<str:tag>',views.hashtag,name="blogsapp_hashtag"),
    path('search/',views.search,name="blogsapp_search"),
    path('<slug:blog_slug>/',views.blog,name="blogsapp_blog"),
    path('',views.index,name="blogsapp_home"),
]
