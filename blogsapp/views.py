from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Blog,Category,Tag,Author
from blogsapp.utils.pagination import build_pagination
from django.core.paginator import Paginator
from django.db.models import Q
from analyticsapp.signals import object_view_signal
from mainapp.utils import seo_utils


NO_OF_RECENT_BLOGS = 3

#blog home page
def index(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'categories':Category.objects.all(),
        'tags': Tag.objects.all(),
        'page_obj': page_obj,
        'recent_blogs':Blog.objects.all().order_by('-created_at')[:NO_OF_RECENT_BLOGS],
        'meta': seo_utils.meta_blog_home(),
    }
    return render(request, 'blogsapp/views/index.html',context=context)

def category(request,name):
    blog_list = Blog.objects.filter(category__name=name)
    paginator = Paginator(blog_list, 6) # Show 6 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'query_category':name,
        'categories':Category.objects.all(),
        'total':len(blog_list),
        'tags': Tag.objects.all(),
        'page_obj': page_obj,
        'recent_blogs':Blog.objects.all()[:NO_OF_RECENT_BLOGS],
        'meta':seo_utils.meta_blog_category(),
    }
    return render(request, 'blogsapp/views/category.html',context=context)

def hashtag(request,tag):
    blog_list = Blog.objects.filter(tags__name=tag)
    paginator = Paginator(blog_list, 6) # Show 6 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'query_tag':tag,
        'total_post':len(blog_list),
        'categories':Category.objects.all(),
        'tags': Tag.objects.all(),
        'page_obj': page_obj,
        'recent_blogs':Blog.objects.all()[:NO_OF_RECENT_BLOGS],
        'meta':seo_utils.meta_blog_hashtag(),
    }
    return render(request, 'blogsapp/views/hashtag.html',context=context)

def search(request):
    query = request.GET.get('s')
    if query and  (len(query) >= 3):  
        blog_list = Blog.objects.filter(
                Q(title__icontains=query) | Q(overview__icontains=query) |  Q(content__icontains=query) 
            ).distinct()
        paginator = Paginator(blog_list, 6) # Show 6 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'categories':Category.objects.all(),
            'tags': Tag.objects.all(),
            'page_obj': page_obj,
            'recent_blogs':Blog.objects.all().order_by('-created_at')[:3],
        }
        return render(request, 'blogsapp/views/search.html',context=context)
    else:
        return redirect("blogsapp:blogsapp_home")
    
def blog(request,blog_slug):
    try:
        blog = Blog.objects.get(slug=blog_slug)
        context ={
            'recent_blogs':Blog.objects.all().order_by('-created_at')[:3],
            'tags':Tag.objects.all(),
            'categories':Category.objects.all(),
            'blog' : blog,
            'meta' : blog.as_meta(),
        }
        #sending object view signal
        object_view_signal.send(sender=blog.__class__ , instance=blog, request=request);
    except:
        pass

    return render(request, 'blogsapp/views/blog_details.html',context=context)

