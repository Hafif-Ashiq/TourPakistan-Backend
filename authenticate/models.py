from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField("mobile", max_length=20)
    name = models.CharField("Name", max_length=400)
    role = models.CharField("Role", default="user", max_length=40)
    email_verified = models.BooleanField("email_verified", default=False)
    phone_verified = models.BooleanField("phone_verified", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
