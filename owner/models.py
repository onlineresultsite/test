from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    logintype = models.CharField(max_length=50)
