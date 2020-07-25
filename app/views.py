from django.shortcuts import render, redirect


def trial(request):
    if request.method == 'GET':
        return "success"
