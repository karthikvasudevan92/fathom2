from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
 	url(r'^$', views.dash, name='dash'),
]
