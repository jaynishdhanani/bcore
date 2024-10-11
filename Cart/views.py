from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Cart
from AdminProduct.models import Product
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# def addtocart(request):
#     qty = request.POST.get("qty")
#     userid = request.user.id
#     pid = request.POST.get("pid")
#     obj = Cart()
#     obj.cart_qty = qty

#     productobj = Product.objects.get(product_id = pid)
#     obj.product_id = productobj

#     userobj = request.user
#     obj.user_id = userobj

#     obj.save()

#     return redirect("/home")

def addtocart(request):
    if request.method == 'GET':
        return render(request,"ProductShop.html")
    else:
        pid = request.POST.get("pid")
        qty = request.POST.get("qty")
        productobj = Product.objects.get(product_id = pid)
        user = request.user

        try:
            cart_item = Cart.objects.get(user_id = user , product_id = productobj)
            cart_item.cart_qty += int(qty)
            cart_item.save()
        except Cart.DoesNotExist:
            Cart.objects.create(
                user_id=user,
                product_id=productobj,
                cart_qty=qty
            )
        return redirect('/product/cart')

def addtocartsingle(request,pid):
    qty = 1
    productobj = Product.objects.get(product_id = pid)
    user = request.user

    try:
        cart_item = Cart.objects.get(user_id = user , product_id = productobj)
        cart_item.cart_qty += int(qty)
        cart_item.save()
    except Cart.DoesNotExist:
        Cart.objects.create(
            user_id=user,
            product_id=productobj,
            cart_qty=qty
        )
    return redirect('/product/cart')
        

def CartProduct(request):
    data = Cart.objects.filter(user_id = request.user.id)
    context={
        "cartdata":data
    }
    return render(request,'Cart.html',context)

def deleteCart(request,id):
    obj = Cart.objects.get(cart_id = id)
    obj.delete()
    return redirect("/product/cart")

@csrf_exempt
def getAllCart(request):
    data = Cart.objects.filter(user_id = request.user.id)
    my_list=list()
    for row in data:
        mydic = {
            "cart_id":row.cart_id,
            "cart_qty":row.cart_qty,
            "product_id":row.product_id.product_id,
            "product_name":row.product_id.product_title,
            "product_image":row.product_id.product_image,
            "product_price":row.product_id.product_price,
        }
        my_list.append(mydic)
    return JsonResponse(my_list,safe=False)