from django.db import models
from clss.models import Clss


class Subject(models.Model):
    clss = models.ForeignKey(Clss,  on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=20, blank = True)
    full_mark = models.IntegerField(max_length=3, null=True)

    def __str__(self):
        return self.sub_name+" "+str(self.clss)






