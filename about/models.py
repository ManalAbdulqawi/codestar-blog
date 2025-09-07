from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class About(models.Model):
    title = models.CharField()
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
     

