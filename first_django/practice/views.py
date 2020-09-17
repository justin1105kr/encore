from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def TellHello(requests):
    html = '<h1> MY first Django App this is. </h1>'
    return HttpResponse(html)