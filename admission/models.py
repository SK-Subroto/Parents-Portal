from django.db import models
from subject.models import Subject
from student.models import Student
from clss.models import Clss

class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    CLS_CHOICES = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five')
    )
    clss = models.CharField(max_length=1, choices=CLS_CHOICES, default="----")
    
    
    def __str__(self):
        return str(self.student)+" "+str(self.subject)
