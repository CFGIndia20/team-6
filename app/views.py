from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.templates import extract_url
from app.templates import demo_predict
from app.templates import prediction
import json
import os
import sys
p = os.getcwd() + '\\get_category_from_image'
sys.path.insert(0, p)

def trial(request):
	if request.method == 'POST':
		url = extract_url.extract(request.body.text)
		context = {
			'latitude': url[0],
			'longitude':url[1]
		}
		return render(request, 'app/form.html', context)

def form(request):
	return render(request, 'app/form.html', context = {})
def reviews(request):
	return render(request, 'app/review.html')


def get_issue(request):
	if request.method == 'POST':
		print('\n\n\n', request)
		imagepath = "".join(map(chr,request.body ))
		with open("img.png", "wb") as f:
			f.write(request.body)
		classes = demo_predict.extract(imagepath)[0]
		print('\n\n\n', classes)
		d = {0:"garbage", 1:"potholes", 2:"stray dogs", 3:"street lights", 4:"traffic jam"}
		ind = classes.index(max(classes))
		return JsonResponse({
		 "prediction": d[ind]
		})
# {"text":"jvdkbjkrbge"}
def getrnn(request):
	if request.method == 'POST':
		with open("rnn.txt", "wb") as f:
			f.write(request.body)
	f = open("rnn.txt", "r")
	text = f.read()
	text = text[1:]
	text = text[:-2]
	text = text.split(":")[1]
	text = text[1:]
	p = prediction.main_predict(text)
	print('pred\n\n', p)
	return JsonResponse({
		"prediction": p
	})

	
		
