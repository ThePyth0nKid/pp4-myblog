from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_login(request):
    return HttpResponse("This is the user login page")
