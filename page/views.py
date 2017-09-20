# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'html/about.html')

def product1(request):
    return render(request, 'html/product1.html')

def product2(request):
    return render(request, 'html/product2.html')

def product3(request):
    return render(request, 'html/product3.html')

def example(request):
    return render(request, 'html/example.html')

def solution(request):
    return render(request, 'html/solution.html')

def join(request):
    return render(request, 'html/join.html')

def contact(request):
    return render(request, 'html/contact.html')

def news_content(request):
    return render(request, 'html/news-content.html')

def dark(request):
    return render(request, 'html/404-dark.html')

def light(request):
    return render(request, 'html/404-light.html')

def news(request):
    return render(request, 'html/news.html')
