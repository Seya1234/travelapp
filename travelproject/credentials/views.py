from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email address already taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                                password1=password1)
                user.save();
        else:
            messages.info(request, "passwords does not match")
            return redirect('credentials:register')
        return redirect('/')
    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        x = request.POST['username']
        y = request.POST['password1']
        user = auth.authenticate(username=x, password=y)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('credentials:login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
