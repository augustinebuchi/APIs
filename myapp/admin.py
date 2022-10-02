from django.contrib import admin
from .models import Customers, Products, Orders

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Orders)