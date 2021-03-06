from django.conf.urls import url, include
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^delete(\d+)$', views.delete),
    url(r'^area$', views.area),
    url(r'^login$', views.login),
    url(r'^loginCheck$', views.loginCheck),
]
