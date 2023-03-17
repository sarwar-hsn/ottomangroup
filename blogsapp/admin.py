from django.contrib import admin
from django import forms
from .models import Author
from .models import Author,Tag,Category,Blog,BlogImages

# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)


class BlogImagesAdmin(admin.StackedInline):
    model = BlogImages

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImagesAdmin]
    def get_form(self, request, obj=None, **kwargs):
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['tags'].widget = forms.CheckboxSelectMultiple()
        return form

admin.site.register(Blog,BlogAdmin)
