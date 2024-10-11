from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="/user/login")
def ChangePass(request):
    if request.method == "GET":
        return render(request,'Changepassword.html')
    else:
        uname = request.user.username
        opassword = request.POST.get("txtoldpass")
        npassword = request.POST.get("txtnewpass")
        user = authenticate(request,username = uname,password = opassword)
        if user is not None:
            user.set_password(npassword)
            user.save()
            messages.success(request, 'Password changed successfully')
            return redirect('/home')
        else:
            messages.error(request, 'Invalid old password')
            return redirect('/changepassword')
