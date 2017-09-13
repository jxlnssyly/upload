#encoding:utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import *
from models import *

def index(request):
    # first = Photo.objects.filter(type='0,')[0]
    # title = first.title
    # list = first.images.all()
    #
    # contex = {
    #     'title': title,
    #     'imageList': list,
    # }
    # return render(request,'imageload/index.html',contex)



    homeList = Photo.objects.filter(type='0,')[0].images.all() #首页轮播图
    photographyList = Photo.objects.filter(type='1,') #摄影
    designList = Photo.objects.filter(type='2,') #设计
    diaryList = Photo.objects.filter(type='3,') #日记

    contex = {
        'photographyList': photographyList,
        'designList': designList,
        'diaryList': diaryList,
        'homeList': homeList
    }
    return render(request,'imageload/index.html',contex)

