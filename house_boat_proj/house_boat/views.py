from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'house_boat/home.html')
