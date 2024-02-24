from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.apps import apps
from django.core import management
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class ToursViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Tour.objects.all()
