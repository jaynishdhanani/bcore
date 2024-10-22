from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

def ViewEmployee(request):
    data = User.objects.all()
    context={
        "employeedata":data,
    }
    return render(request,'Employee.html',context)

def AddEmployee(request):
    if request.method == "GET":
        return render(request,'AddEmployee.html')
    else:
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email Already Registered!")
                return redirect("/add/emolyee")
            else:
                user = User.objects.create_user(username=email,email=email,password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                messages.success(request,"Register Successfully!")
                return redirect("/view/employee")
        except Exception as e:
            messages.error(request,"Something goes wrong! Please contact u admin"+str(e))
            return redirect("/add/employee")