from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="List name", max_length=250)