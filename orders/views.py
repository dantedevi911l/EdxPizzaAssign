from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def index(request):
    #return HttpResponse("Project 3: TODO")
    return render(request, "login.html")


def my_login(request):
	if request.user.is_authenticated:
		# Authenticated user
		return HttpResponse("Logged In user")
	else:
		#Anonymous user
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			# below method attaches authenticated user to Django's session
			login(request,user)
			return HttpResponse("Successfully Logged In")
		else:
			return HttpResponse("Invalid Login")


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
