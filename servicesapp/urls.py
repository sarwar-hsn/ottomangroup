from django.urls import path
from . import views

app_name = 'servicesapp'


urlpatterns = [
    path('',views.home,name="servicesapp_home"),
    path('study-in-turkey/',views.study,name="servicesapp_study"),
    path('study-in-turkey/packages',views.study_packages,name="servicesapp_study_packages"),
    path('real-estate-and-consultancy/',views.real_estate,name="servicesapp_real_estate"),
    path('properties',views.property,name="servicesapp_properties"),
    path('property-details/<slug:prop_slug>',views.prop_details,name="servicesapp_property_details"),
    path('hajj-and-umrah',views.hajj_umrah,name="servicesapp_hajj_umrah"),
    path('citizenship-and-residence-permit',views.citizenship,name="servicesapp_citizenship"),
    path('export-import',views.export_import,name="servicesapp_export_import"),
    path('service-solutions',views.service_solutions,name="servicesapp_service_solutions"),
    path('tourism-and-health-tourism',views.tourism,name="servicesapp_tourism"),
   
]
