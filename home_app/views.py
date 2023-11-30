from django.shortcuts import render 
from django.http import HttpResponse


def home(request):
    return render(request,"home_app/home.html")


def contactus(request):
    return HttpResponse("Hi This Is Contact us Page")

def aboutus(request):
    return HttpResponse("HI THIS PAGE IS ABOUTUS")