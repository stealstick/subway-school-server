from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from .models import Station, StationWay 
from rest_framework import viewsets  
from rest_framework.decorators import api_view
from .serializers import UserSerializer, GroupSerializer, StationSerializer, StationWaySerializer, FilterSerializer
import requests

class UserViewSet(viewsets.ModelViewSet):  
    """
    사용자(user)를 보거나 편집하는 API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):  
    """
    그룹(group)을 보거나 편집하는 API
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StationViewSet(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

class StationWayViewSet(viewsets.ModelViewSet):
    serializer_class = StationWaySerializer
    queryset = StationWay.objects.all()

class FilterViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def view(request):
          return Response({"message": "Hello for today! See you tomorrow!"})
    serializer_class = FilterSerializer
    queryset = StationWay.objects.all()
    #queryset = StationWay.objects.filter(station_way__in=)
