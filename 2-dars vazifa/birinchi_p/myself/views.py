from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest):
    return HttpResponse('<h3 style="text-align: center">Salom saytimizga hush kelibsiz!!!</h3>')

def contact(request: HttpRequest):
    return HttpResponse('<h5 style="text-align: left"><a href="https://t.me/nurulloh_303">Telegam orqali aloqa😊</a></h5>')

def instagram(request: HttpRequest):
    return HttpResponse('<a href="https://www.instagram.com/nurulloh_303/">Instagram kanalimizga obuna boling😊</a>')