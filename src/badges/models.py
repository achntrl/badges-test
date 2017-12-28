from django.contrib.auth.models import User
from django.db import models


class Star(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Collector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Pioneer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PowerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
