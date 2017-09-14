# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def index(request):
    template = loader.get_template('/var/www/whqj/page/templates/index.html')
    return HttpResponse(template)
