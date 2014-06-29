__author__ = 'Administrator'

from django.conf.urls import patterns,url
import views

urlpatterns = patterns('',
    url(r'^createUser$', views.createUser),
    # url(r'^findAllUsers$', views.findAllUsers),
    url(r'^$', views.index),

)