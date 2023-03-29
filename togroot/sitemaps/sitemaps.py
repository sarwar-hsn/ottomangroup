from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blogsapp.models import Blog,Category
from servicesapp.models import Property

class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'
    protocol = 'https'
    def items(self):
        return [
            'mainapp:mainapp_index',
            'mainapp:mainapp_contact',
            'mainapp:mainapp_about',
            'servicesapp:servicesapp_home',
            'formsapp:formsapp_apply_study',
            'formsapp:formsapp_book_consultancy',
            'blogsapp:blogsapp_home'
        ]
    
    def location(self, item):
        return reverse(item)

class ServicesSiteMap(Sitemap):
    priority = .9
    changefreq = 'daily'
    protocol = 'https'
    def items(self):
        return [
            'servicesapp:servicesapp_study',
            'servicesapp:servicesapp_real_estate',
            'servicesapp:servicesapp_hajj_umrah',
            'servicesapp:servicesapp_citizenship',
            'servicesapp:servicesapp_export_import',
            'servicesapp:servicesapp_service_solutions',
            'servicesapp:servicesapp_tourism',
        ]
    def location(self, item):
        return reverse(item)


class BlogsSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'
    
    def items(self):
        return Blog.objects.filter(status="published").order_by('-created_at').distinct()

    def lastmod(self,obj):
        return obj.last_modified
    
    def location(self, obj):
        return '/blogs/%s' % (obj.slug)


class PropertiesSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Property.objects.all().order_by('-created_at').distinct()

    def lastmod(self,obj):
        return obj.last_modified
    
    def location(self, obj):
        return obj.get_absolute_url()

class CategorySiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def lastmod(self,obj):
        return obj.last_modified
    
    def location(self, obj):
        return obj.get_absolute_url()