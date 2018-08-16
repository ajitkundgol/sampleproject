from django.shortcuts import render
from django.http import HttpResponse
from login.models import *
from django.core import serializers
from django.db import connection


# Create your views here.
def registration_login(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	emailid = request.POST.get('email','')

	reg1 = registration.objects.all()

	if request.method == "POST":
		reg = registration()
		reg.user_name = username
		reg.password = password
		reg.email = emailid
		reg.save()

	return render(request, 'register.html', {'reg':reg1 })

