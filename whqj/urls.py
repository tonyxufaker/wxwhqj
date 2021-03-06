"""whqj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from page import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'about', views.about, name='about'),
    url(r'^index', views.index, name='index'),
    url(r'product1', views.product1, name='product1'),
    url(r'product2', views.product2, name='product2'),
    url(r'product3', views.product3, name='product3'),
    url(r'example', views.example, name='example'),
    url(r'solution', views.solution, name='solution'),
    url(r'join', views.join, name='join'),
    url(r'contact', views.contact, name='contact'),
    url(r'news-content', views.news_content, name='news-content'),
    url(r'404-dark', views.dark, name='404-dark'),
    url(r'404-light', views.light, name='404-light'),
    url(r'news', views.news, name='news')
]
