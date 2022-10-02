#from http.client import REQUEST_ENTITY_TOO_LARGE
from django.http import JsonResponse
from .models import Customers, Products
from .serializers import CustomerSerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render

# Create your views here.
#@api_view(['GET','POST'])
def Customer_list(request, format=None):
    customers = Customers.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return JsonResponse({'Customers': serializer.data}, #safe=False
    )

@api_view(['GET','POST'])
def product_list(request, format=None):

    if request.method == 'GET':

        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({'Products': serializer.data}, #safe=False - for representing your data as list
        )

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def product_detail(request, id, format=None):
    
    try:
       prod = Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(prod)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









@api_view(['GET','PUT', 'DELETE'])
def order_hist(request):


    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
