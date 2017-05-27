# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
        messages.success(request, "Not Created")
    context = {
    "form": form,
    }
    return render(request, "post_form.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title" : "List"
    }
    return render(request, "index.html", context)

def post_detail(request, id):
    instance = get_object_or_404(Post, id = id)
    context = {
        "instance": instance,
        "title" : "Detaili9999",
    }
    return render(request, "post_detail.html", context)

def post_update(request, id =None):
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
        messages.success(request, "Not Edited")
    context = {
        "title": instance.title,
        "form": form,
        "instance": instance,
    }
    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
