from django.contrib.auth.backends import ModelBackend
from .models import CustomerUser, Doctor
from django.contrib.auth import authenticate
from django.contrib.auth.backends import BaseBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomerUser.objects.get(email=username)
        except CustomerUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None