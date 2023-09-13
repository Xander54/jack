from django.db import models

# Create your models here.
class Phonebook(models.Model):
    phone_number=models.CharField(max_length=12,blank=True)
class User(models.Model):
    email=models.EmailField(blank=True)
    comment=models.CharField(max_length=200)
