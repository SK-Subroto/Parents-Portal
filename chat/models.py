from django.db import models
from users.models import User

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)

    def __unicode__(self):
        return self.message
