import ast
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


@api_view(["GET"])
def get_location(request, id):
    location = Location.objects.get(id=id)
    serializer = LocationSerializer(location)
    return Response(serializer.data)


@api_view(["GET"])
def get_tour(request, id):
    tour = Tour.objects.get(id=id)
    serializer = TourSerializer(tour)
    return Response(serializer.data)


class ToursViewSet(ModelViewSet):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()


@api_view(["POST"])
def add_location_to_tours(request):
    data = request.data
    tour = Tour.objects.get(id=data["tour_id"])
    locations = data["locations"]

    locations = ast.literal_eval(locations)

    # serializer = TourSerializer(tour)

    for loc in locations:
        tour.locations.add(loc)

    return Response({"status": True})
