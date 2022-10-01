from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=25)
    Password = models.SlugField(max_length=500)
    address = models.CharField(max_length=70)

class Products(models.Model):
    name = models.CharField(max_length=20)
    GovtApprovedID = models.IntegerField(max_length=200)
    ExpiryDate = models.DateField(max_length=12)

class Order(models.Model):
