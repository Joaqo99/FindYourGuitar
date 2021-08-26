from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import List
from .forms import CreateNewList

def mylists(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            l = List(name=n)
            l.save()
            
    form = CreateNewList()
    my_dict = {"lists":List.objects.all(), "form":form}
    return render(response, "list_tracker/mylists.html", my_dict)