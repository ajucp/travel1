from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,reviewer

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=reviewer.objects.all()
    return render(request,"index.html",{'result':obj,'review':obj1})

def credential(request):
    return  render(request,"registration.html")

def addition(request):
    return render(request,'add.html')