from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.templates import extract_url

def trial(request):
	extract_url.extract()
	return render(request, 'app/form.html')
