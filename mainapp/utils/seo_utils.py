from mainapp.models import seo
from meta.views import Meta
from mainapp.utils import seo_utils

def meta_home():
    seo_obj = seo.objects.filter(page='home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
            
        )
        return meta


def meta_about():
    seo_obj = seo.objects.filter(page='about')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_contact():
    seo_obj = seo.objects.filter(page='contact')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_services_home():
    seo_obj = seo.objects.filter(page='services_home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta


def meta_real_estate():
    seo_obj = seo.objects.filter(page='real_estate')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta


def meta_citizenship():
    seo_obj = seo.objects.filter(page='citizenship')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_study():
    seo_obj = seo.objects.filter(page='study')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_study_packages():
    seo_obj = seo.objects.filter(page='study_packages')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_export_import():
    seo_obj = seo.objects.filter(page='export_import')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_hajj_umrah():
    seo_obj = seo.objects.filter(page='hajj_umrah')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_service_solutions():
    seo_obj = seo.objects.filter(page='service_solutions')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta


def meta_tourism():
    seo_obj = seo.objects.filter(page='tourism')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_property_home():
    seo_obj = seo.objects.filter(page='property_home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_blog_home():
    seo_obj = seo.objects.filter(page='blog_home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_blog_category():
    seo_obj = seo.objects.filter(page='blog_category')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_blog_hashtag():
    seo_obj = seo.objects.filter(page='blog_hashtag')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_apply_education():
    seo_obj = seo.objects.filter(page='apply_education')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_book_consultancy():
    seo_obj = seo.objects.filter(page='book_consultancy')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta