from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    documents = models.FileField(upload_to='documents', blank=True)