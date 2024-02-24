from .views import *
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path("location", LocationViewSet.as_view()),
    path("tours", ToursViewSet.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
