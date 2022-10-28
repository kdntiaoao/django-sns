from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from snsapp.models import SnsModel

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return render(request, "signup.html", {})
        except IntegrityError:
            return render(request, "signup.html", {"error": "すでに登録されています"})

    return render(request, "signup.html", {})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("list")
        else:
            return render(request, "login.html", {})

    return render(request, "login.html", {})


def list(request):
    object_list = SnsModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})
