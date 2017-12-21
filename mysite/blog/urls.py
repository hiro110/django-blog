#!coding:utf-8
#from django.conf.urls import patterns, url
#from blog import views
#
#urlpatterns = patterns('',
#        url(r'^$', views.show, name='show'),
#        url(r'^edit/$', views.edit, name='edit'),
#)


from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.show, name='show'),
    path('edit/', views.edit, name='edit'),
]