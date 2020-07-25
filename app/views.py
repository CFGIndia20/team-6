from django.shortcuts import render, redirect
from django.http import HttpResponse

def trial(request):
	if request.method == 'GET':
		print("GETT")
		return HttpResponse("<p> success </p>")
