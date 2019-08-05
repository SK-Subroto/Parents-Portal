from django.db import models
from django.utils import timezone
from student.models import Student
# from teacher.models import Teacher
from users.models import User

class Meeting(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    message = models.TextField()
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.student.stu_id} {self.message}'
