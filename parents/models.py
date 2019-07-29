from django.db import models
# from django.contrib.auth.models import User
from student.models import Student
from django.urls import reverse
from parents_portal import settings
from users.models import User

class Parents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    relation = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length = 50)
    address = models.TextField()

    def __str__(self):
        return f'{self.user.username} {self.name}'

    def save(self, *args, **kwargs):
        super(Parents, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('parents-profile', kwargs={"pk": self.pk})
