from django.shortcuts import render
from django.http import HttpResponse
from servicesapp.utils import service_utils
from .utils import faqs
from formsapp.forms import ContactForm
from blogsapp.models import Blog
from mainapp.utils import seo_utils

# Create your views here.
    
def index(request):
    featured_blogs = Blog.objects.filter(featured=True).order_by('view_count')[:6]
    context={
        'services':service_utils.all_services,
        'chooseus':[
            'Honesty',
            'Teamwork',
            'Reliability',
            'Professionalism'
        ],
        'featured_blogs':featured_blogs,
        'meta':seo_utils.meta_home(),
    }
    return render(request, 'mainapp/views/index.html',context=context)


def about(request):
    context={
        'faqs': faqs.about_faqs,
        'faqs_length':range(1,len(faqs.about_faqs)+1),
        'meta':seo_utils.meta_about(),
    }
    return render(request, 'mainapp/views/about.html',context= context)


def contact(request):
    context={
        'form':ContactForm,
        'meta':seo_utils.meta_contact(),
    }
    return render(request, 'mainapp/views/contact.html',context=context)


def error_404_view(request, exception):
    return render(request, 'mainapp/views/page_not_found.html')