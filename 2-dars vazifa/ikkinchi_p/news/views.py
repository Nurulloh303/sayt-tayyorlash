from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def home(request: HttpRequest):
    return HttpResponse("Hello world")

def savol(request: HttpRequest):
    return HttpResponse('<h3>Har qanday savolingizni yozishingiz mumkin</h3>'
                        '<input type="text" placeholder="Savolingizni kiriting">')

def kurs(request: HttpRequest):
    return HttpResponse('<h4>Qaysi kursda oqimoqchisiz</h4>'
                        '<select>'
                        '<option value="1">Python</option>'
                        '<option value="2">Java</option>'
                        '<option value="3">C++</option>'
                        '</select>')