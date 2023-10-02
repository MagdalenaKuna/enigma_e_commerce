from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    SALESMAN = 1
    CLIENT = 2

    ROLE_CHOICES = (
        (SALESMAN, "Salesman"),
        (CLIENT, "Client"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
