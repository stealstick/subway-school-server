"""subway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers  
from subwayapi import views

router = routers.DefaultRouter()  
router.register(r'users', views.UserViewSet)  
router.register(r'groups', views.GroupViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'stationways', views.StationWayViewSet)


urlpatterns = [  
    url(r'^', include(router.urls)),    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]