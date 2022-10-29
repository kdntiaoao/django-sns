from django.urls import path
from .views import signup, login, list, logout, detail

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("list/", list, name="list"),
    path("logout/", logout, name="logout"),
    path("detail/<int:pk>", detail, name="detail"),
]
