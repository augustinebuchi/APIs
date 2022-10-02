from rest_framework import serializers
from .models import Customers, Orders, Products

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        field = ['id', 'name', 'phone', 'order', 'address']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        field = ['id', 'name', 'company', 'GovtApprovedID', 'ExpiryDate']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        field = ['customer', 'product', 'quantity', 'company', 'address']

