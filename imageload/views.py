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




    return render(request,'imageload/index.html',getBaseData())

def photography(request):

    return render(request,'imageload/photography.html',getBaseData())

def design(request):

    return render(request,'imageload/photography.html')

def diary(request):

    return render(request,'imageload/photography.html')

def content(request,id):
    objc = Photo.objects.filter(pk=id).first().images.all()
    contex = getBaseData()
    contex['obj'] = objc
    return render(request,'imageload/content.html',contex)

def getBaseData():

    homeList = Photo.objects.filter(advertisement=True) #首页轮播图
    photographyList = Photo.objects.filter(type='1,') #摄影
    designList = Photo.objects.filter(type='2,') #设计
    diaryList = Photo.objects.filter(type='3,') #日记

    contex = {
        'photographyList': photographyList,
        'designList': designList,
        'diaryList': diaryList,
        'homeList': homeList
    }

    return contex

