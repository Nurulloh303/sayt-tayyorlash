from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from .models import Brad, Car
# Create your views here.


def home(request: HttpRequest):
    return HttpResponse("Salom")

def brand(request: HttpRequest):
    brands = Brad.objects.all()

    context = {
        "brands": brands,
    }

    return render(request, "autosalon/index.html", context)

