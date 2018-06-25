from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo
from booktest.models import HeroInfo
from datetime import date
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
# Create your views here.

def index(request,pIndex):
    b_list = BookInfo.objects.all()
    p = Paginator(b_list,10)
    if pIndex == '':
        pIndex ='1'
    pIndex=int(pIndex)
    booklist = p.page(pIndex)
    plist = p.page_range
    context={'booklist':booklist,'plist':plist,'pIndex':pIndex}
    return  render(request,'booktest/index.html',context)

def detail(request):
    # herolist = HeroInfo.objects.all()
    #context = {'herolist': herolist}
    context = {'test': '<h1>haha<h1>'}

    return render(request, 'booktest/detail.html', context)

def create(request):
    book=BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995,12,30)
    book.save()
    #转向到首页
    #return redirect('/booktest')
    return redirect(reverse('booktest:index'))

def delete(request,id):
    book=BookInfo.objects.get(id=int(id))
    book.delete()
    #转向到首页
    return redirect('/booktest')

def json1(request):
    return JsonResponse({'h1':'hello','h2':'world'})

def my_ajax(request):
    return render(request,'booktest/my_ajax.html')


def my_static(request):
    return render(request,'booktest/my_static.html')