from django.shortcuts import render
from django.http import HttpResponse
from .models import Search, Guitar
from .forms import GuitarSearch
from .scrapper import search_articles

# Create your views here.
def index(response):
    return render(response, "finder/index.html", {})

def search(response):
    if response.method == "POST":
        search_form = GuitarSearch(response.POST)
        if search_form.is_valid():
            no_results = False
            guitar_brand = search_form.cleaned_data["brand"]
            guitar_model = search_form.cleaned_data["g_model"]
            guitar_list = search_form.cleaned_data["g_list"]
            search_group = Search()
            search_group.save()
            search_articles(guitar_brand, guitar_model, guitar_list, search_group, Guitar)
            if search_group.guitar_set.all().count() == 0:
                no_results = True
            return render(response, "finder/search.html", {"search_form":search_form, "search_group":search_group, "no_results":no_results})
    else:
        search_form = GuitarSearch()
        no_results = False
        return render(response, "finder/search.html", {"search_form":search_form, "no_results":no_results})