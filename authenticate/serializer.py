from rest_framework import serializers
from .models import *
import re
from django.apps import apps


from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "name",
            "phone",
            "role",
            "email_verified",
            "phone_verified",
        ]
        # exclude = [""]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"], role=validated_data["role"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
