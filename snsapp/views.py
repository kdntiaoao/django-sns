from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
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
            return redirect("list")
        except IntegrityError:
            return render(request, "signup.html", {"errors": {"username": "すでに登録されています"}})

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
            return render(
                request,
                "login.html",
                {"errors": {"username": "ログインに失敗しました", "password": "ログインに失敗しました"}},
            )

    return render(request, "login.html", {})


@login_required
def list(request):
    object_list = SnsModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})

def logout(request):
    auth_logout(request)
    return redirect('login')