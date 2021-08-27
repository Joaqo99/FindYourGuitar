from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="", max_length=250, widget=forms.TextInput(attrs={"placeholder":"List name"}))