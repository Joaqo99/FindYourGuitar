from django.shortcuts import render
from django.http import HttpResponse
from .models import List, Guitar

# Create your views here.
def index(response):
    return render(response, "finder/index.html", {})

def search(response):
    return render(response, "finder/search.html", {})

def lists(response, id):
    g_list = List.objects.get(id=id)
    return render(response, "finder/lists.html", {"name":g_list.name})
