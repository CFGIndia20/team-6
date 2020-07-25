from django.shortcuts import render, redirect
from django.http import HttpResponse
from .templates import extract_url

def trial(request):
	url = extract_url.extract("the link to the location is https://www.google.com/maps/place/Charai+Hindu+Samshaan+Bhoomi/@19.0492292,72.8922557,18z/data=!4m5!3m4!1s0x3be7c8a8d4029427:0x991bade397542b3a!8m2!3d19.049521!4d72.8932652")
	context = {'lati':url[0],'long':url[1]}
	return render(request, 'app/form.html',context)
