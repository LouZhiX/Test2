from django.shortcuts import render, redirect
from booktest.models import BookInfo, HeroInfo, AreaInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'books':books})

def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bput_date = date(1998, 10, 23)
    b.save()
    #重定向
    return HttpResponseRedirect('/index')

def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return redirect('/index')

def area(request):
    #潜江市上级地区：
    areaParent = AreaInfo.objects.get(areaName='潜江市')
    Parent = areaParent.areaParent

    #潜江市下级地区：
    areaChild = AreaInfo.objects.filter(areaParent__areaName='潜江市')

    return render(request, 'booktest/area.html', {'Parent' : Parent, 'areaChild':areaChild})
