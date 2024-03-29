from django.db import models
# from django.contrib.auth.models import User
from users.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    
