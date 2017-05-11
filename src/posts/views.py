# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.
def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title" : "List"
    }
    # if request.user.is_authenticated():
    #    context = {
    #     "title"  : "My User List"
    #     }
    # else:
    #     context = {
    #         "title"  : "Common List"
    #     }
    return render(request, "index.html", context)

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    # instance = Post.objects.get(id=4)
    instance = get_object_or_404(Post, id = 1)
    context = {
        "instance": instance,
        "title" : "Detaili9999",
    }
    return render(request, "post_detail.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")
def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
