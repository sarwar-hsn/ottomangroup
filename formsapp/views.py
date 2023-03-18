from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EducationForm,ConsultancyForm, ContactForm
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from mainapp.utils import seo_utils

def edu_apply(request):
    if request.POST:
        form = EducationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            mail_body = obj.get_property_values()
            try:
                send_mail(
                    'Education application',
                    mail_body,
                    'it@ottomangrp.com',
                    ['info@ottomangrp.com'],
                )
                messages.success(request, "we received your request. we will contact soon")
                return redirect("formsapp:formsapp_apply_study")
            except:
                messages.error(request, "form submission failed")
            return redirect("formsapp:formsapp_apply_study")
    else:
        context={
            'form':EducationForm(),
            'meta':seo_utils.meta_apply_education()
        }
        return render(request, 'formsapp/edu_apply.html',context=context)

def book_consultancy(request):
    if request.POST:
        form = ConsultancyForm(request.POST)
        if form.is_valid():
            obj = form.save()
            mail_body = obj.get_property_values()
            try:
                send_mail(
                    'free consultancy query',
                    mail_body,
                    'it@ottomangrp.com',
                    ['info@ottomangrp.com'],
                )
                messages.success(request, "we received your request. we will contact soon")
                return redirect("formsapp:formsapp_book_consultancy")
            except:
                messages.error(request, "form submission failed")
            return redirect("formsapp:formsapp_book_consultancy")
    else:
        context={
            'form':ConsultancyForm(),
            'meta':seo_utils.meta_book_consultancy(),
        }
        return render(request,'formsapp/book_consultancy.html',context=context)


def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                obj = form.save()
                mail_body = obj.get_property_values()
                send_mail(
                    'contact query',
                    mail_body,
                    'it@ottomangrp.com',
                    ['info@ottomangrp.com'],
                )
                messages.success(request, "we received your request. we will contact soon")
                return redirect("mainapp:mainapp_contact")
        except:
            messages.error(request, "form submission failed")
    return redirect("mainapp:mainapp_contact")