from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import List
from .forms import CreateNewList

def mylists(response):
    if response.method == "POST":
        if response.POST.get("createList"):
            form = CreateNewList(response.POST)
            if form.is_valid():
                n = form.cleaned_data["name"]
                l = List(name=n)
                l.save()

        elif response.POST.get("deleteList"):
            guitarList_id = response.POST["deleteList"].rsplit('_')[1]
            guitarList = List.objects.get(id=guitarList_id)
            guitarList.delete()

        elif response.POST.get("deleteItems"):
            guitarList_id = response.POST["deleteItems"].rsplit('_')[1]
            guitarList = List.objects.get(id=guitarList_id)
            for guitar in guitarList.guitar_set.all() :
                if response.POST.get("d" + str(guitar.id)) == "delete":
                    guitar.delete()

    form = CreateNewList()
    my_dict = {"lists":List.objects.all(), "form":form}
    return render(response, "list_tracker/mylists.html", my_dict)