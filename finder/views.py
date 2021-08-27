from django.shortcuts import render
from django.http import HttpResponse
from .models import Guitar
from .forms import GuitarSearch
from .scrapper import search_articles

# Create your views here.
def index(response):
    return render(response, "finder/index.html", {})

def search(response):
    if response.method == "POST":
        search_form = GuitarSearch(response.POST)
        if form.is_valid():
            guitar_brand = form.cleaned_data["brand"]
            guitar_model = form.cleaned_data["g_model"]

            results = search_articles(guitar_brand, guitar_model, Guitar)
    else:
        search_form = GuitarSearch()
    return render(response, "finder/search.html", {"search_form":search_form, "results":results})