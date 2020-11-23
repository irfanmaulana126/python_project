from django.shortcuts import render
from django.http import HttpResponse

def login(req):
    return render(req,"backend/login.html")

def regis(req):
    return render(req,"backend/register.html")

def dash(req):
    return render(req,"backend/dashboard.html")