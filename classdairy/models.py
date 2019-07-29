from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from users.models import User

class Classdairy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now=False, auto_now_add=False)
    content = models.TextField()
    SUB_CHOICES = (
        ('B', 'Bangla'),
        ('E', 'English'),
    )
    subject = models.CharField(max_length=1, choices=SUB_CHOICES, default="E")
    check = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.content

    @property
    def get_html_url(self):
        url = reverse('classdairy:calender-detail', args=(self.id,))
        return f'<a href="{url}"> {self.author} {self.subject} </a>'
    # def get_absolute_url(self):
    #     return reverse("user-view-classdairy", })
    

