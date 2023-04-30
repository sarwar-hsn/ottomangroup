"""togroot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from .sitemaps import sitemaps as smap

sitemaps={
    'static':smap.StaticViewSitemap(),
    'services':smap.ServicesSiteMap(),
    'blogs':smap.BlogsSiteMap(),
    'properties':smap.PropertiesSiteMap(),
    'categories':smap.CategorySiteMap(),
}

admin.site.site_header = "Ottoman Group"
admin.site.site_title = "TOG Admin Portal"
admin.site.index_title = "Welcome to TOG"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('services/',include('servicesapp.urls',namespace='servicesapp')),
    path('blogs/',include('blogsapp.urls',namespace='blogsapp')),
    path('forms/',include('formsapp.urls',namespace='formsapp')),
    path('auth/',include('django.contrib.auth.urls')),
    path('',include('mainapp.urls',namespace='mainapp')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG is True:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'mainapp.views.error_404_view'