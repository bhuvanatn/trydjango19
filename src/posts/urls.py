from django.conf.urls import url
from django.contrib import admin

from posts import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.post_list, name='post_list'),
    url(r'^create/$', posts_views.post_create, name='post_create'),
    url(r'^detail/$', posts_views.post_detail, name='post_detail'),
    url(r'^update/$', posts_views.post_update, name='post_update'),
    url(r'^delete/$', posts_views.post_delete, name= 'post_delete'),
]