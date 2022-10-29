from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from snsapp.models import SnsModel

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            auth_login(request, user)
            return redirect("list")
        except IntegrityError:
            return render(
                request, "signup.html", {"errors": {"username": "すでに登録されています"}}
            )

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
    return redirect("login")


@login_required
def detail(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    return render(request, "detail.html", {"object": object})


@login_required
def good(request, pk):
    object = SnsModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect("detail", pk=pk)


@login_required
def read(request, pk):
    user_id = str(request.user.id)
    object = get_object_or_404(SnsModel, pk=pk)
    readed_user_list = object.readText.split(",")

    # 既読済みのユーザーのとき
    if user_id in readed_user_list:
        readed_user_list.remove(user_id)
        object.read -= 1
    # 未既読のユーザーのとき
    else:
        readed_user_list.append(user_id)
        object.read += 1

    object.readText = ",".join(readed_user_list)
    object.save()

    return redirect("detail", pk=pk)


class SnsCreateView(LoginRequiredMixin, CreateView):
    template_name: str = "create.html"
    model = SnsModel
    fields = ("title", "content", "author")
    success_url = reverse_lazy("list")
