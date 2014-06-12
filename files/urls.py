__author__ = 'Administrator'
from django.conf.urls import patterns,url
import views


urlpatterns = patterns('',
    url(r'^uploadFile/$', views.uploadFile),
    url(r'^$', views.index),
)
