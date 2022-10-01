from django.http import JsonResponse
from .models import User
from .models import Products
from .serializer import UserSerializer
from .serializers import ProductsSerializer
from django.shortcuts import render

# Create your views here.
def user_list(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return JsonResponse(serializer.data, safe=False)

def product_list(request):
    prod = Products.objects.all()
    serializer = ProductsSerializer(Products, many=True)
    return JsonResponse(serializer.data, safe=False)
