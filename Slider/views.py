from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
from django.core.files.storage import FileSystemStorage
from .models import Slider
import os
from django.conf import settings

# Create your views here.
def ViewSlider(request):
    data = Slider.objects.all()
    context={
        "sliderdata":data
    }
    return render(request,'ViewSlider.html',context)


def SliderPage(request):
    if request.method == "GET":
        return render(request,'AddSlider.html')
    else:
        # form value get
        slidertitle = request.POST.get("slider_title")
        slidersubtitle = request.POST.get("slider_subtitle")
        buttontext = request.POST.get("slider_button_text")
        buttonurl = request.POST.get("slider_button_url")
        # Image Upload 
        extesion = os.path.splitext(str(request.FILES['sliderimage']))[1]
        filename = get_random_string(length=32) + extesion 
        sliderimg = request.FILES.get("sliderimage")
        fss = FileSystemStorage()
        file = fss.save(filename,sliderimg)
        file_url = fss.url(file)

        # Insert

        obj = Slider()
        obj.slider_title = slidertitle
        obj.slider_subtitle = slidersubtitle
        obj.slider_button_text = buttontext
        obj.slider_button_url = buttonurl
        obj.slider_image = file_url
        obj.save()
        return redirect('/view/slider')
    
def UpdateSlider(request,id):
    if request.method == "GET":
        data = Slider.objects.get(slider_id = id)
        context = {
            "data":data
        }
        return render(request,'UpdateSlider.html',context)
    else:
        
        imgname = request.POST.get("oldimg")
        if request.FILES.get("sliderimage"):
            # Remove Old Image
            path = imgname
            image_name = path.split('/')[-1]
            os.remove(os.path.join(settings.MEDIA_ROOT, image_name))

            # Image Upload 
            extesion = os.path.splitext(str(request.FILES['sliderimage']))[1]
            filename = get_random_string(length=32) + extesion 
            sliderimg = request.FILES.get("sliderimage")
            fss = FileSystemStorage()
            file = fss.save(filename,sliderimg)
            imgname = fss.url(file)

        # Update

        obj = Slider.objects.get(slider_id = id)
        obj.slider_title = request.POST.get("slider_title")
        obj.slider_subtitle = request.POST.get("slider_subtitle")
        obj.slider_button_text = request.POST.get("slider_button_text")
        obj.slider_button_url = request.POST.get("slider_button_url")
        obj.slider_image = imgname
        obj.save()
        return redirect('/view/slider')
    
def DeleteSlider(request,id):
    obj = Slider.objects.get(slider_id = id)
    path = obj.slider_image
    image_name = path.split('/')[-1]
    os.remove(os.path.join(settings.MEDIA_ROOT, image_name))
    obj.delete()
    return redirect("/view/slider")