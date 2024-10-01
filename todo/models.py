from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=50,blank=False)
    desccription = models.TextField(max_length=1200,default="no description")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)