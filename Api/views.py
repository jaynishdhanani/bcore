from django.shortcuts import render
from rest_framework import viewsets
from AdminProduct.models import Product
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def getAllProducts(request):
    result = Product.objects.all()
    data = []
    for obj in result:
        data.append({
            'product_title': obj.product_title,
            'product_price': obj.product_price,
            'product_videourl': obj.product_videourl,
            'product_description': obj.product_description,
            'product_specification': obj.product_specification,
            'product_isactive': obj.product_isactive,
            'product_image': obj.product_image,
        })
    return Response(data)

@api_view(['GET'])
def getSingleProducts(request,id):
    result = Product.objects.filter(product_id = id)
    data = []
    for obj in result:
        data.append({
            'product_title': obj.product_title,
            'product_price': obj.product_price,
            'product_videourl': obj.product_videourl,
            'product_description': obj.product_description,
            'product_specification': obj.product_specification,
            'product_isactive': obj.product_isactive,
            'product_image': obj.product_image,
        })
    return Response(data)