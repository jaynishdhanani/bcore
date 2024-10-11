from django.shortcuts import render,redirect
from AdminProduct.models import Product
from Cart.models import Cart
from AdminState.models import State
from AdminCity.models import City
from Order.models import Order
from Items.models import Items
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def Checkoutpage(request):
    if request.method == "GET":
        data = Cart.objects.filter(user_id = request.user.id)
        statedata = State.objects.all()
        citydata = City.objects.all()
        total=0
        for row in data:
            total = total + row.total_price
        context={
            "cartdata":data,
            "subtotal":total,
            "statedata":statedata,
            "citydata":citydata
        }
        return render(request,'Checkout.html',context)
    else:
        amount = float(request.POST.get('amt')) * 100
        order_currency = 'INR'
       
        
        order = client.order.create({
            'amount': amount,
            'currency': order_currency, 
            'payment_capture': '1'
        })

      
        context = {
            'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
            'amount': amount,
            'currency': order_currency,
            'order_id': order['id'],
            "fname": request.POST.get('fname'),
            "lname": request.POST.get('lname'),
            "email": request.POST.get('email'),
            "phone": request.POST.get('phone'),
            "fnaddressame": request.POST.get('address'),
            "shipping_charge": request.POST.get('shipping_charge'),
            "subtotal": request.POST.get('subtotal'),
            "amt": request.POST.get('amt'),
            "number": request.POST.get('number'),
            "city": request.POST.get('city'),
            'callback_url': '/createOrder'
        }

        return render(request, 'payment.html', context)

        
@csrf_exempt
def createOrder(request):
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    zipcode = request.POST.get('number')
    cid = request.POST.get("city")
    shipping_charge_order = request.POST.get("shipping_charge")
    subtotal_order = request.POST.get("subtotal")
    finaltotal_order = request.POST.get("amt")

    
    obj = Order()
    obj.user_id = request.user
    obj.city_id = City.objects.get(city_id = cid)
    obj.first_name = first_name
    obj.last_name = last_name
    obj.email = email
    obj.phone = phone
    obj.address = address
    obj.zipcode = zipcode
    obj.shipping_charge_order = shipping_charge_order
    obj.subtotal_order = subtotal_order
    obj.finaltotal_order = finaltotal_order

    obj.save()

    cartdata = Cart.objects.filter(user_id = request.user.id)
    for row in cartdata:
        itemobj = Items()
        itemobj.order_id = obj
        itemobj.qty = row.cart_qty
        itemobj.product_id = row.product_id
        itemobj.product_price = row.product_id.product_price
        itemobj.save()
        row.delete()

    return redirect('/home')