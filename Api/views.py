from django.shortcuts import render
from rest_framework import viewsets
from AdminProduct.models import Product
from Order.models import Order
from Items.models import Items
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['GET'])
def getAllUser(request):
    result = User.objects.all()
    data = []
    for obj in result:
        data.append({
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'username': obj.username,
        })
    return Response(data)




@api_view(['POST'])
@csrf_exempt
def UserLogin(request):
    uname = request.POST.get("username")
    pwd = request.POST.get("password")
    user = authenticate(request,username = uname,password = pwd)
    if user is not None:
        return JsonResponse({'status':'success','message':'Log In successfully!','data':{
            'name':user.username,
            'userid':user.id
        }})
    else:
        return JsonResponse({'status':'Error','message':'Username or Password not found'})




@api_view(['GET'])
def getAllProducts(request):
    result = Product.objects.all()
    data = []
    for obj in result:
        data.append({
            'product_id': obj.product_id,
            'product_title': obj.product_title,
            'product_price': obj.product_price,
            'product_videourl': obj.product_videourl,
            'product_description': obj.product_description,
            'product_specification': obj.product_specification,
            'product_isactive': obj.product_isactive,
            'product_image': "http://127.0.0.1:8000" + obj.product_image,
        })
    return Response(data)

@api_view(['GET'])
def getSingleProducts(request,id):
    result = Product.objects.filter(product_id = id)
    data = []
    for obj in result:
        data={
            'product_id': obj.product_id,
            'product_title': obj.product_title,
            'product_price': obj.product_price,
            'product_videourl': obj.product_videourl,
            'product_description': obj.product_description,
            'product_specification': obj.product_specification,
            'product_isactive': obj.product_isactive,
            'product_image': "http://127.0.0.1:8000" + obj.product_image,
        }
    return Response(data)

@api_view(['GET'])
def getAllOrder(request):
    result = Order.objects.all()
    data = []
    for obj in result:
        data.append({
            'order_id': obj.order_id,
            'user_id': obj.user_id.id,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'phone': obj.phone,
            'status': obj.status,
            'address': obj.address,
            'city_name': obj.city_id.city_name,
            'zipcode': obj.zipcode,
            'order_datetime': obj.order_datetime,
            'shipping_charge_order': obj.shipping_charge_order,
            'subtotal_order': obj.subtotal_order,
            'finaltotal_order': obj.finaltotal_order,
        })
    return Response(data)

@api_view(['GET'])
def getSingleOrder(request,id):
    result = Order.objects.filter(order_id = id)
    data = []
    for obj in result:
        data={
            'order_id': obj.order_id,
            'user_id': obj.user_id.id,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'phone': obj.phone,
            'status': obj.status,
            'address': obj.address,
            'city_name': obj.city_id.city_name,
            'zipcode': obj.zipcode,
            'order_datetime': obj.order_datetime,
            'shipping_charge_order': obj.shipping_charge_order,
            'subtotal_order': obj.subtotal_order,
            'finaltotal_order': obj.finaltotal_order,
        }
    return Response(data)

@api_view(['GET'])
def getSingleItemProduct(request,id):
    result = Items.objects.filter(order_id = id)
    data = []
    for obj in result:
        data.append({
            'product_id': obj.product_id.product_id,
            'product_title': obj.product_id.product_title,
            'product_price': obj.product_price,
            'qty': obj.qty,
            'total_price': obj.total_price,
        })
    return Response(data)

@api_view(['POST'])
def UpdateOrder(request,id):
    try:
        status = request.POST.get("status")
        obj = Order.objects.get(order_id = id)
        obj.status = status
        obj.save()
        return JsonResponse({"status":True,"message":"Status Updated"}) 
    except Exception as e:   
        return JsonResponse({"status":False,"message":"error"}) 