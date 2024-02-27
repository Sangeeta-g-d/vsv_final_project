from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class contact(models.Model):
    
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    contact_no = models.CharField(max_length=300)
    
    
    message = models.CharField(max_length=1000)
