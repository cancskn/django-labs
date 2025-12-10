from django import forms

class BookReviewForm(forms.Form):
    nickname = forms.CharField(max_length=50)
    rate = forms.IntegerField(min_value=0, max_value=100)
    review = forms.CharField(widget=forms.Textarea)
    contains_spoilers = forms.BooleanField(required=False)
