from django.shortcuts import render,redirect
from .utils import service_utils,edu_utils,realestate_utils,tourism_utils
from blogsapp.models import Blog
from .models import Property,PropertyImages
from django.core.paginator import Paginator
from django.db.models import Q
from mainapp.utils import seo_utils
from django.shortcuts import get_object_or_404

#services home page
def home(request):
    context={
        'services': service_utils.all_services, 
        'meta': seo_utils.meta_services_home()
        
    }
    return render(request, 'servicesapp/views/index.html',context=context)


#study/education home page
def study(request):
    featured_blogs = Blog.objects.filter(featured=True).order_by('view_count')[:6]
    blog = Blog.objects.filter(slug='why-students-should-come-to-turkiye');
    
    if blog:
        blog = blog[0];
    context={
        'faqs': edu_utils.faqs,
        'featured_blogs':featured_blogs,
        'why_turkey_blog': blog,
        'working_process':edu_utils.working_process,
        'meta': seo_utils.meta_study(),
        'university_types':edu_utils.university_types,
    }
    return render(request, 'servicesapp/views/study.html',context=context)
#this is study package page
def study_packages(request):
    context={
        'package_table':edu_utils.pacakge_table,
        'services':edu_utils.services,
        'meta':seo_utils.meta_study_packages(),
    }
    return render(request, 'servicesapp/views/study_packages.html',context=context) 
#real-estate home page
def real_estate(request):
    blog = Blog.objects.filter(slug='investment-opportunities-turkish-real-estate');
    if blog:
        blog = blog[0];
    context={
        'featured_properties':Property.objects.all().order_by('-created_at')[:5],
        'services':realestate_utils.services,
        'package_table':realestate_utils.pacakge_table,
        'blog':blog,
        'meta': seo_utils.meta_real_estate(),
    }
    return render(request, 'servicesapp/views/real-estate.html',context=context)

#properties home page
def property(request):
    query = request.GET.get('s')
    if query:
        property_list = Property.objects.filter(
                Q(title__icontains=query) 
                | Q(description__icontains=query) 
                | Q(property_type__icontains=query) 
                | Q(city__icontains=query)
                | Q(state__icontains=query)
                | Q(address__icontains=query)
                | Q(amenities__icontains=query)
            ).distinct()
    else:
        property_list = Property.objects.all()
    paginator = Paginator(property_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj': page_obj,
        'meta': seo_utils.meta_property_home()
    }
    return render(request, 'servicesapp/views/properties.html',context=context)


def prop_details(request,prop_slug):
    try:
        property = Property.objects.get(slug=prop_slug)
        model_dict = property.get_model_dictionay()
        context={
            'property':property,
            'gallery': PropertyImages.get_gallery_images(property),
            'tabledict': model_dict,
            'meta':property.as_meta()
        }
    except:
        property = None
        context={}
    return render(request, 'servicesapp/views/property_details.html',context=context)


#hajj umrah section
def hajj_umrah(request):
    context={
        'meta': seo_utils.meta_hajj_umrah(),
    }
    return render(request, 'servicesapp/views/hajj.html',context=context)

#citizenship
def citizenship(request):
    context={
        'meta': seo_utils.meta_citizenship(),
    }
    return render(request, 'servicesapp/views/citizenship.html',context=context)

#def export-import
def export_import(request):
    context={
        'meta': seo_utils.meta_export_import(),
    }
    return render(request, 'servicesapp/views/export-import.html',context=context)

#service solution
def service_solutions(request):
    context={
        'meta': seo_utils.meta_service_solutions(),
    }
    return render(request, 'servicesapp/views/service-solutions.html',context=context)


#tourism
def tourism(request):
    context={
        'pacakges':tourism_utils.packages,
        'meta': seo_utils.meta_tourism(),
    }
    return render(request, 'servicesapp/views/tourism.html',context=context)