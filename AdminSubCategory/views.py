from django.shortcuts import render,redirect
from django.conf import settings
from .models import SubCategory
from AdminCategory.models import Category


def customsubadmin(request):
    data = SubCategory.objects.all()
    context={
        "subcategorydata":data
    }
    return render(request,'subcategory.html',context)

def addSubcategory(request):
    if request.method == "GET":
        data = Category.objects.all()
        context = {
            "catdata":data
        }
        return render(request,'addsubcategory.html',context)
    else:
        cid = request.POST.get("txtcategory")
        obj = SubCategory()
        obj.subcategory_name = request.POST.get("txtname")
        obj.subcategory_description = request.POST.get("txtdescription")
        obj.category_id = Category.objects.get(category_id = cid)
        obj.save()
        return redirect('/back/subcategory')
    
def deleteSubCategory(request,id):
    obj = SubCategory.objects.get(subcategory_id = id)
    obj.delete()
    return redirect("/back/subcategory")

def updateSubCategory(request,id):
    if request.method == "GET":
        catdata = Category.objects.all()
        data = SubCategory.objects.get(subcategory_id = id)
        context = {
            "data":data,
            "catdata":catdata
        }
        return render(request,'updatesubcategory.html',context)
    else:
        cid = request.POST.get("txtcategory")

        obj = SubCategory.objects.get(subcategory_id = id)
        obj.subcategory_name = request.POST.get("txtname")
        obj.subcategory_description = request.POST.get("txtdescription")
        obj.category_id = Category.objects.get(category_id = cid)
        obj.save()
    return redirect("/back/subcategory")