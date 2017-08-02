from django.contrib.auth.models import User, Group  
from rest_framework import serializers
from .models import Station, StationWay

class UserSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = Group
        fields = ('url', 'name')



class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class StationWaySerializer(serializers.ModelSerializer):
    class Meta:
        model = StationWay
        fields = '__all__'