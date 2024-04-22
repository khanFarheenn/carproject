from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serilalizer import CarSerializer,OwnerSerializer
# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer