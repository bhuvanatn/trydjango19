# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_home(request):
    return HttpResponse("<h1>Hello</h1>")
