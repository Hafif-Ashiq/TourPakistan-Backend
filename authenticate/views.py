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


class RegisterUser(APIView):
    def post(self, request):
        # try:
        data = request.data
        data["role"] = "agency"

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data["email"])
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"status": 200, "data": serializer.data, "token": str(token_obj)}
            )
        return Response(serializer.errors)

    # except Exception as e:
    #     print(e)
    #     return Response({"status": str(e)})

    def patch(self, request):
        try:
            obj = User.objects.get(email=request.data["email"])

            serializer = UserSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "data": serializer.data,
                    }
                )
            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({"status": "Error"})


class LoginUser(APIView):
    def post(self, request):
        # try:
        print(request.data)
        username = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            token_obj, _ = Token.objects.get_or_create(user=user)
            user_object = User.objects.get(email=user)
            serializer = UserSerializer(user_object)
            return Response(
                {
                    "status": True,
                    "role": serializer.data["role"],
                    "token": str(token_obj),
                }
            )
        return Response({"status": False})

    # except Exception as e:
    #     print(e)
    #     return Response({"status": False})


class RegisterAgency(APIView):
    def post(self, request):
        # try:
        data = request.data
        data["role"] = "agency"
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data["email"])
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"status": 200, "data": serializer.data, "token": str(token_obj)}
            )
        return Response(serializer.errors)

    # except Exception as e:
    #     print(e)
    #     return Response({"status": str(e)})

    def patch(self, request):
        try:
            obj = User.objects.get(email=request.data["email"])

            serializer = UserSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "data": serializer.data,
                    }
                )
            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({"status": "Error"})


class RegisterBusiness(APIView):
    def post(self, request):
        # try:
        data = request.data
        data["role"] = "business"
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data["email"])
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"status": 200, "data": serializer.data, "token": str(token_obj)}
            )
        return Response(serializer.errors)

    def patch(self, request):
        try:
            obj = User.objects.get(email=request.data["email"])

            serializer = UserSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "data": serializer.data,
                    }
                )
            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({"status": "Error"})
