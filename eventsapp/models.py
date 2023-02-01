from django.db import models

# Create your models here.
class user(models.Model):
    userid=models.AutoField(primary_key=True)
    uname = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contactno = models.IntegerField()