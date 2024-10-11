from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import os
from django.conf import settings
from .models import Category

def customadmin(request):
    data = Category.objects.all()
    context={
        "categorydata":data
    }
    return render(request,'category.html',context)

def AddCategory(request):
    if request.method == "GET":
        return render(request,'addcategory.html')
    else:
        # form value get
        name = request.POST.get("txtname")
        # Image Upload 
        extesion = os.path.splitext(str(request.FILES['txtimg']))[1]
        filename = get_random_string(length=32) + extesion 
        categoryimg = request.FILES.get("txtimg")
        fss = FileSystemStorage()
        file = fss.save(filename,categoryimg)
        file_url = fss.url(file)

        # Insert

        obj = Category()
        obj.category_name = name
        obj.category_image = file_url
        obj.save()
        return redirect('/back/category')
    
def deleteCategory(request,id):
    obj = Category.objects.get(category_id = id)
    path = obj.category_image
    image_name = path.split('/')[-1]
    os.remove(os.path.join(settings.MEDIA_ROOT, image_name))
    obj.delete()
    return redirect("/back/category")

def updateCategory(request,id):
    if request.method == "GET":
        data = Category.objects.get(category_id = id)
        context = {
            "data":data
        }
        return render(request,'updatecategory.html',context)
    else:
        imgname = request.POST.get("txtimg")
        if request.FILES.get("txtimage"):
            # Remove Old Image
            path = imgname
            image_name = path.split('/')[-1]
            os.remove(os.path.join(settings.MEDIA_ROOT, image_name))

            # Image Upload 
            extesion = os.path.splitext(str(request.FILES['txtimage']))[1]
            filename = get_random_string(length=32) + extesion 
            categoryimg = request.FILES.get("txtimage")
            fss = FileSystemStorage()
            file = fss.save(filename,categoryimg)
            imgname = fss.url(file)

        obj = Category.objects.get(category_id = id)
        obj.category_name = request.POST.get("txtname")
        obj.category_image = imgname
        obj.save()

    return redirect("/back/category")