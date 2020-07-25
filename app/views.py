from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.templates import extract_url
from app.get_category_from_image import demo_predict
# p = os.getcwd() + '\\get_category_from_image'
# sys.path.insert(0, p)

def trial(request):
	extract_url.extract()
	return render(request, 'app/form.html')

def reviews(request):
	return render(request, 'app/review.html')


def get_issue(imagepath):
	classes = demo_predict.extract(imagepath)[0]
	print('\n\n\n', classes)
	d = {0:"garbage", 1:"potholes", 2:"stray dogs", 3:"street lights", 4:"traffic jam"}
	ind = classes.index(max(classes))
	return d[ind]
