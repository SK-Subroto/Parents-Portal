from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length = 50)
    address = models.TextField()
    designation = models.CharField(max_length = 20)

    def __str__(self):
        return f'{self.user.username} {self.name}'

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)
