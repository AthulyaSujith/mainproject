from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from datetime import date, datetime
from django.urls import reverse





# Create your views here.
def loginn(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd = request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request, user)
            return render(request, "student.html")
        else:
            messages.info(request," Username or pawssord is incorrect")
            return render(request,"loginn.html")
    return render(request,"loginn.html")

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pwd']
        cpassword = request.POST['cpwd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return render(request, "signup.html")


            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return render(request, "loginn.html")
            print("User created")
        else:
            messages.info(request, "password not matching")
            return render(request, "signup.html")
        return redirect('/')
    return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')



def student(request):
    return render(request, "student.html")





'''def rsform(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # gender = request.POST.get('gender')
        rforms = reg(fname=fname, lname=lname, dob=dob, age=age, email=email)
        rforms.save()
        if fname or lname or dob or age or email:
            messages.info(request, 'At least one field is not empty.')
            return render(request, "testform.html")
        return render(request, "confirm.html")

    return render(request, "testform.html")'''







def demo(request):
    return render(request,"indexes.html")

def about(request):
    return render(request,"about.html")


'''
if request.method == 'POST':
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    dob = request.POST.get('dob')
    age = request.POST.get('age')
    email = request.POST.get('email')

    # gender = request.POST.get('gender')
    rforms = reg(fname=fname, lname=lname, dob=dob, age=age, email=email)
    rforms.save()
    if fname or lname or dob or age or email:
        messages.info(request, 'At least one field is not empty.')
    return render(request, "confirm.html")

return render(request, "testform.html")

return render(request, "testform.html")'''




