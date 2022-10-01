from django.contrib import admin
from .models import User
from .models import Products

admin.site.register(User)
admin.site.register(Products)