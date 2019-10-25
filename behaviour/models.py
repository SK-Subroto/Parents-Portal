from django.db import models
# from django.contrib.auth.models import User
from student.models import Student
from users.models import User
from django.utils import timezone

class Behavior (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now=False, auto_now_add=False)
    A_CHOICES = (
        (1, 'Class Response'),
        (2, 'Fight'),
        (3, 'Misbehave'),
    )
    catagory = models.IntegerField(max_length=1, choices=A_CHOICES, default="1")
    B_CHOICES = (
        (-1, 'very Bad'),
        (-2, 'Bad'),
        (0,'Normal'),
        (1, 'Good'),
        (2, 'Very Good'),
    )
    scale = models.IntegerField(max_length=1, choices=B_CHOICES, default="0")
    content = models.TextField()
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Behaviour_assess(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_post = models.DateTimeField(default=timezone.now)
    classAttention = models.IntegerField()
    behaveTeacher = models.IntegerField()
    behaveStudent = models.IntegerField()
    attenClass = models.IntegerField()
    performance = models.IntegerField()