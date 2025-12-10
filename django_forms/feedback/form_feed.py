from django import forms

class FeedbackForm(forms.Form):
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()
    stars = forms.IntegerField(min_value=1, max_value=5)
    description = forms.CharField(widget=forms.Textarea)