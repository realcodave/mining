from django.db import models

# Create your models here.


class User(models.Model):
    Username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
