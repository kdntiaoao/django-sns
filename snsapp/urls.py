from django.urls import path
from .views import signup, login, list

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("list/", list, name="list"),
]
