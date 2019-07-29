from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

