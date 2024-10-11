from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import os
from django.conf import settings
from .models import Product
from django.http import HttpResponse
from AdminSubCategory.models import SubCategory


def adminproduct(request):
    data = Product.objects.all()
    context={
        "productdata":data
    }
    return render(request,'product.html',context)

def addProduct(request):
    if request.method == "GET":
        data = SubCategory.objects.all()
        context = {
            "subcatdata":data
        }
        return render(request,'addproduct.html',context)
    else:
        # form value get
        product_title = request.POST.get("producttitle")
        product_price = request.POST.get("productprice")
        product_videourl = request.POST.get("productvideourl", None)
        product_description = request.POST.get("productdescription")
        product_specification = request.POST.get("productspecification")
        product_isactive = request.POST.get("productisactive")
        # Image Upload 
        extesion = os.path.splitext(str(request.FILES['productimage']))[1]
        filename = get_random_string(length=32) + extesion 
        productimg = request.FILES.get("productimage")
        fss = FileSystemStorage()
        file = fss.save(filename,productimg)
        file_url = fss.url(file)

        # Insert
        subcid = request.POST.get("txtsubcategory")
        obj = Product()
        obj.product_title = product_title
        obj.product_price = product_price
        obj.product_videourl = product_videourl
        obj.product_description = product_description
        obj.product_specification = product_specification
        obj.product_isactive = product_isactive
        obj.product_image = file_url
        obj.subcategory_id = SubCategory.objects.get(subcategory_id = subcid)
        obj.save()
        return redirect('/back/product')
    
def deleteProduct(request,id):
    obj = Product.objects.get(product_id = id)
    path = obj.product_image
    image_name = path.split('/')[-1]
    os.remove(os.path.join(settings.MEDIA_ROOT, image_name))
    obj.delete()
    return redirect("/back/product")

def updateProduct(request,id):
    if request.method == "GET":
        subcatdata = SubCategory.objects.all()
        data = Product.objects.get(product_id = id)
        context = {
            "data":data,
            "subcatdata":subcatdata
        }
        return render(request, 'updateproduct.html',context)
    else:
        # Form value get
        product_title = request.POST.get("producttitle")
        product_price = request.POST.get("productprice")
        product_videourl = request.POST.get("productvideourl", None)
        product_description = request.POST.get("productdescription")
        product_specification = request.POST.get("productspecification")
        product_isactive = request.POST.get("productisactive") == 'True'

        imgname = request.POST.get("productimage")
        obj = Product.objects.get(product_id = id)
        if request.FILES.get("productimage"):
            # Remove Old Image
            path = imgname
            image_name = path.split('/')[-1]
            os.remove(os.path.join(settings.MEDIA_ROOT, image_name))

            extesion = os.path.splitext(str(request.FILES['productimage']))[1]
            filename = get_random_string(length=32) + extesion 
            productimg = request.FILES.get("productimage")
            fss = FileSystemStorage()
            file = fss.save(filename,productimg)
            file_url = fss.url(file)
            obj.product_image = file_url


            # Update the product with new values
        subcid = request.POST.get("txtsubcategory")
        obj.product_title = product_title
        obj.product_price = product_price
        obj.product_videourl = product_videourl
        obj.product_description = product_description
        obj.product_specification = product_specification
        obj.product_isactive = product_isactive
        obj.subcategory_id = SubCategory.objects.get(subcategory_id = subcid)
        obj.save()
        return redirect('/back/product')
    
def changeStatus(request,id,status):
    obj = Product.objects.get(product_id = id)
    if status == "Yes":
        obj.product_isactive = 0
    else:
        obj.product_isactive = 1
    obj.save()
    return redirect('/back/product')