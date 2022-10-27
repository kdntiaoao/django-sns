from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render

# Create your views here.


def signup(request):
    # object = User.objects.get(username="tanaka")
    # print(object.password)

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, "signup.html", {"error": "すでに登録されています"})
    # else:
    #     print("this is not post method")

    return render(request, "signup.html", {})
