from rest_framework import serializers
from .models import *
import re
from django.apps import apps


from django.contrib.auth.models import User


class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    images = LocationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ["name", "history", "city"]
        # exclude = [""]

    def create(self, validated_data):
        uploaded_data = validated_data.pop("uploaded_images")
        new_location = Location.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            new_product_image = LocationImage.objects.create(
                location=new_location, images=uploaded_item
            )
        return new_location


class TourSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Location
        fields = "__all__"
        extra_kwargs = {"locations": {"required": False}}
