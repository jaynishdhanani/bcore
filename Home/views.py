from django.shortcuts import render,redirect
from AdminProduct.models import Product
from AdminCategory.models import Category
from Slider.models import Slider
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail

def Homepage(request):
    last4productdata = Product.objects.all().order_by('-product_id')[:4]
    data = Category.objects.all()
    sdata = Slider.objects.all()
    context={
        "categorydata":data,
        "last4productdata":last4productdata,
        "sliderdata":sdata
    }
    return render(request,'Home.html',context)

def AboutProduct(request):
    return render(request,'About.html')

def ContactProduct(request):
    return render(request,'Contact.html')

def ShopProduct(request):
    if request.method == "GET":
        products = Product.objects.filter(product_isactive=1)
        data = Category.objects.all()
        context = {
            "categorydata":data,
            "productData":products
        }
        return render(request,'ProductShop.html',context)
    else:
        min = float(request.POST.get("min"))
        max = float(request.POST.get("max"))
        products = Product.objects.filter(product_price__range=(min,max))
        data = Category.objects.all()
        context = {
            "categorydata":data,
            "productData":products
        }
        return render(request,'ProductShop.html',context)

def UserProfile(request):
    return render(request,'UserProfile.html')

def UserLogin(request):
    if request.method == "GET":
        return render(request,'Login.html')
    else:
        oemail = request.POST.get("txtemail")
        opassword = request.POST.get("txtpassword")
        user = authenticate(request,username = oemail,password = opassword)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request,"Username or Password not found")
            return redirect('/user/login')

def CreateAccount(request):
    if request.method == "GET":
        return render(request,'CreateAccount.html')
    else:
        ofirstname = request.POST.get("txtfirstname")
        olastname = request.POST.get("txtlastname")
        oemail = request.POST.get("txtemail")
        opassword = request.POST.get("txtpassword")
        try:
            if User.objects.filter(email=oemail).exists():
                messages.error(request,"Email Already Registered!")
                return redirect("/createaccount")
            else:
        
                user = User.objects.create_user(username=oemail,email=oemail,password=opassword)
                user.first_name = ofirstname
                user.last_name = olastname
                user.save()
                # Loggedin the user
                login(request,user)
                subject = "Welcome!"
                message = "Welcome to the site"
                send_mail(
                    subject,
                    message,
                    'jaynishdhanani8@gmail.com',
                    [oemail],
                    fail_silently=False,
                    )
                messages.success(request,"Register Successfully!")
                return redirect("/home")
        except Exception as e:
            messages.error(request,"Something goes wrong! Please contact u admin"+str(e))
            return redirect("/createaccount")

def UserLogout(request):
    logout(request)
    return redirect('/user/login')  



def InfoProduct(request,id):
    data = Product.objects.get(product_id = id)
    context = {
        "productData":data,
        "pid":id
    }
    return render(request,'Productinfo.html',context)

def CategoryByProducts(request,catid):
    if request.method == "GET":
        data = Category.objects.all()
        products = Product.objects.filter(product_isactive=1,subcategory_id__category_id = catid)
        context = {
            "productData":products,
            "categorydata":data,
        }
        return render(request,'CategoryByProducts.html',context)
    else:
        min = float(request.POST.get("min"))
        max = float(request.POST.get("max"))
        data = Category.objects.all()
        products = Product.objects.filter(product_isactive=1,subcategory_id__category_id = catid,product_price__range=(min,max))
        context = {
            "productData":products,
            "categorydata":data,
        }
        return render(request,'CategoryByProducts.html',context)