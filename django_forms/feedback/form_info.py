from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)
