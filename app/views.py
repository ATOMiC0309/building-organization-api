from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Area, Building, Organization
from .serializers import AreaSerializer, BuildingSerializer, OrganizationSerializer
from rest_framework import permissions
from rest_framework import viewsets


class BuildingAPIView(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AreaAPIView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganizationAPIView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]