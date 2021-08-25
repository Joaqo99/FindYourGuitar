from django.shortcuts import render
from django.http import HttpResponse
from .models import Guitar

# Create your views here.
def index(response):
    return render(response, "finder/index.html", {})

def search(response):
    return render(response, "finder/search.html", {})