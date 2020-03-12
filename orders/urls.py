from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.my_login, name="login"),
    path("signup/", views.my_signup, name="signup")
]
