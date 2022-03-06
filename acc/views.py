from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def index(request) :
    return render (request, "acc/index.html")

def login_user(request) :
    if request.method == "POST" :
        un = request.POST.get("uname")
        pw = request.POST.get("upass")
        user = authenticate(username=un, password=pw)
        if user :
            login(request, user)
            return redirect("acc:index")
        else :
            pass
    return render(request, "acc/login.html")

def logout_user(request) :
    logout(request)
    return redirect ("acc:login")

def signup(request) :
    if request.method == "POST" :
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get ("ucom")
        pi = request.FILES.get("upic")
        try :
            User.objects.create_user(username=un, password=up, age=ua, comment=uc, pic=pi)
            return redirect("acc:login")
        except :
            pass
    return render (request, "acc/signup.html")
