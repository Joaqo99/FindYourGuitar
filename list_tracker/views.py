from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import List

def mylists(response):
    return render(response, "list_tracker/mylists.html", {"lists":List.objects.all()})