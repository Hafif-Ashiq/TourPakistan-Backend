from .views import *
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path("location", LocationViewSet.as_view({"get": "list", "post": "create"})),
    path("tours", ToursViewSet.as_view({"get": "list", "post": "create"})),
    path("add-location-to-tour", add_location_to_tours),
    path("get-location/<id>", get_location),
    path("get-tour/<id>", get_tour),
]
