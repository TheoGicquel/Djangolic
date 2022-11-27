from django import forms
from django.forms import ModelForm
from .models import Beer, Glass, Country, Style, Type, Brewery

class SearchBeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ('name','ibu','abv','glass','type','style','countries_sold_in')