from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HTTP_response(reqest):
    return HttpResponse("hello world")

