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

# Django 1.10 no longer allows you to specify views as a string (e.g. 'myapp.views.home') in your URL patterns.
#
# The solution is to update your urls.py to include the view callable. This means that you have to import the view in your urls.py. If your URL patterns don't have names, then now is a good time to add one, because reversing with the dotted python path no longer works.
#
# from django.contrib.auth.views import login
# from myapp.views import home, contact
#
# urlpatterns = [
#     url(r'^$', home, name='home'),
#     url(r'^contact/$', contact, name='contact'),
#     url(r'^login/$', login, name='login'),
# ]
# If there are many views, then importing them individually can be inconvenient. An alternative is to import the views module from your app.
#
# from django.contrib.auth import views as auth_views
# from myapp import views as myapp_views
#
# urlpatterns = [
#     url(r'^$', myapp_views.home, name='home'),
#     url(r'^contact/$', myapp_views.contact, name='contact'),
#     url(r'^login/$', auth_views.login, name='login'),
# ]
