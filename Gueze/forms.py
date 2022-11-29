from django import forms
from django.forms import ModelForm
from .models import Beer, Glass, Country, Style, Type, Brewery
#! TODO : Try to add tailwind classes to forms
# beer
class BeerSearchForm(ModelForm):
    class Meta:
        model = Beer
        fields = ('name','ibu','abv','glass','type','style','countries_sold_in','srm')
        
class BeerCreateForm(ModelForm):
    class Meta:
        model = Beer
        fields = ('name','ibu','abv','glass','type','style','countries_sold_in','taste','image','srm')

# brewery

class BreweryCreateForm(ModelForm):
    class Meta:
        model = Brewery
        fields = ('name','country','beers')

class BrewerySearchForm(ModelForm):
    class Meta:
        model = Brewery
        fields = ('name','country')



# country
class CountryCreateForm(ModelForm):
    class Meta:
        model = Country
        fields = ('name',)

class CountrySearchForm(ModelForm):
    class Meta:
        model = Country
        fields = ('name',)



class BeerCreateForm(ModelForm):
    class Meta:
        model = Beer
        fields = ('name','ibu','abv','glass','type','style','countries_sold_in','taste','image','srm')
