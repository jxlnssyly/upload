#encoding:utf-8
from django.contrib import admin
from models import *
from django import forms

# class PhotoAdmin(admin.ModelAdmin):
class TypeForm(forms.ModelForm):
    TYPE = (
        ('0', '首页轮播广告'),
        ('1', '摄影'),
        ('2', '设计'),
        ('3', '日记'),
    )

    def clean_type(self):
        field = ""
        for data in self.cleaned_data['type']:
          field += str(data)+","
        return field.lstrip(",")

    type = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=TYPE, initial="1")

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    form = TypeForm
    inlines = [ PropertyImageInline, ]

admin.site.register(Photo,PropertyAdmin)

