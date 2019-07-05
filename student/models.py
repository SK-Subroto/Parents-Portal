from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f'{self.user.username} {self.name}'

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)