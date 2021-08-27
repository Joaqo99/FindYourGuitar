from django import forms
from list_tracker.models import List

class GuitarSearch(forms.Form):

    brand = forms.CharField(label="", max_length=250, widget=forms.TextInput(attrs={"placeholder":"Brand"}))
    g_model = forms.CharField(label="", required=False, max_length=250, widget=forms.TextInput(attrs={"placeholder":"Model"}))
    g_list = forms.ModelChoiceField(label="", widget=forms.Select, queryset=List.objects.all())