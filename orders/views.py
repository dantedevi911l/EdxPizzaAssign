from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from orders.models import *


# Create your views here.
def index(request):
    #return HttpResponse("Project 3: TODO")
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("order"))
    else:
        return render(request, "login.html")


def my_login(request):
    if request.user.is_authenticated:
        # Authenticated user
        return HttpResponseRedirect(reverse("order"))
    else:
        # Anonymous username
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # below method attached authenticated user to Django's session
            login(request,user)
            return HttpResponseRedirect(reverse("order"))
        else:
            return HttpResponse("User does not exist")


def my_signup(request):

	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	try:
		user = User.objects.get(username=username)
		# send the user to login page with a message
		context = {
			'message': "User already exists. Please Select a new user name"
		}
		return render(request,"login.html",context)
	except User.DoesNotExist:
		user = User.objects.create_user(username, email, password)
		user.first_name = firstname
		user.last_name = lastname
		user.save()
		return HttpResponseRedirect(reverse("index"))


def my_order(request):
    if request.user.is_authenticated:
        pizzas = Pizza.objects.all()
        pizza_dict = {}
        pizza_size = []
        for pizza in pizzas:
            type = pizza.get_type_display()
            sub_type = pizza.sub_type
            topping_quantity = pizza.topping_quantity
            size = pizza.get_size_display()
            price = pizza.price
            if type not in pizza_dict:
                pizza_dict[type] = {}
            if sub_type not in pizza_dict[type]:
                pizza_dict[type][sub_type] = {}
            if topping_quantity not in pizza_dict[type][sub_type]:
                pizza_dict[type][sub_type][topping_quantity] = {}
            if size not in pizza_dict[type][sub_type][topping_quantity]:
                pizza_dict[type][sub_type][topping_quantity][size] = {}
            if size not in pizza_size:
                pizza_size.append(size)
            pizza_dict[type][sub_type][topping_quantity][size] = price

        context = {
            'pizzas': pizza_dict,
            'sizes': pizza_size
        }
        return render(request,"menuOrder.html",context)
    else:
        return HttpResponseRedirect(reverse("login"))
