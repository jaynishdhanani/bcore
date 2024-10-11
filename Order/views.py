from django.shortcuts import render
from .models import Order


def Orderinfo(request):
    data = Order.objects.filter(user_id = request.user.id)
    context = {
        "orderdata":data,
    }
    return render(request,'Order.html',context)