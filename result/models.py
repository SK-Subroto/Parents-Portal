from django.db import models
from admission.models import Admission

class Result(models.Model):
    admission_id = models.ForeignKey(Admission, on_delete=models.CASCADE)
    first_mark = models.IntegerField(max_length=3, default=0)
    second_mark = models.IntegerField(max_length=3, default=0)
    third_mark = models.IntegerField(max_length=3, default=0)

    def __str__(self):
        return str(self.admission_id)
