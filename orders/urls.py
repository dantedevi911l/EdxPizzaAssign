from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.my_signup, name="signup"),
    path("login/", views.my_login, name="login"),
    path("order/", views.my_order, name="order")
]
