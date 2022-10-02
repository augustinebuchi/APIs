from unittest.util import _MAX_LENGTH
from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=200)
    Phone = models.IntegerField(20)
    email = models.EmailField(max_length=25)
    Password = models.SlugField(max_length=500)
    address = models.CharField(max_length=70)

class Products(models.Model):
    Name = models.CharField(max_length=20)
    Company = models.CharField(max_length=50)
    GovtApprovedID = models.IntegerField(max_length=200)
    ExpiryDate = models.DateField(max_length=12)

class Orders(models.Model):
    NameOfProd = models.CharField(max_length = 200)
    Date = models.DateField(max_length=10)
    Time = models.TimeField(max_length=12)
    Buyer = models.CharField(max_length=50)
    Destination = models.SlugField(max_length=100)
