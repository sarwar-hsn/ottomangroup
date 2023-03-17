from django.core.paginator import Paginator
def build_pagination(request,itemlist,iter_per_page):
    paginator = Paginator(itemlist, iter_per_page)
    page_num = request.GET.get('page',1)
    try:
        if int(page_num) <= 0:
            page_num = 1
        elif int(page_num) > paginator.num_pages:
            page_num = paginator.num_pages
    except:
        page_num = 1;
    try:
        page_obj = paginator.get_page(page_num)
    except:
        page_obj = []
    return page_obj


    
