from rest_framework import serializers
from .models import *
import re
from django.apps import apps


from django.contrib.auth.models import User


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"
        # exclude = [""]


class TourSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Tour
        fields = "__all__"
        extra_kwargs = {"locations": {"required": False}}
