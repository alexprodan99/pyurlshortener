from django import forms
from .models import ShortenerItem

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(attrs={"class": "form-control"}))

    class Meta:
        model = ShortenerItem
        fields = ('long_url',)
