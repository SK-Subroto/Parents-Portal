from django.db import models

class Clss(models.Model):
    class_name = models.CharField(max_length=50)
    num_of_sub = models.IntegerField(max_length=10)

    def __str__(self):
        return self.class_name