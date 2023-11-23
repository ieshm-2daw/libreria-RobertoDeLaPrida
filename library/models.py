from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    dni = models.CharField(max_length=10)
    direcction = models.CharField(max_length=100)
    telf = models.PositiveIntegerField()

    

    def __str__(self):
        return self.username
