from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Fruit

def demo(request):
    obj=Place.objects.all()
    obj2 = Fruit.objects.all()
    return render(request,"index.html",{'result':obj, 'result2':obj2})



def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    r=x+y
    return render(request,"result.html",{'res':r})

def home(request):
    return render(request,"home.html")