from django import forms
from .models import Beer, Glass, Country, Style, Type, Brewery

class BeerSearchForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ('name', 'ibu', 'abv', 'glass', 'type', 'style', 'countries_sold_in', 'brewery')

        

class BeerCreateForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ('name', 'ibu', 'abv', 'glass', 'type', 'style', 'countries_sold_in', 'brewery', 'taste', 'image', 'srm')

class BeerUpdateForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ('id', 'name', 'ibu', 'abv', 'glass', 'type', 'style', 'countries_sold_in', 'brewery', 'taste', 'image', 'srm')



# brewery

class BreweryCreateForm(forms.Form):
    class Meta:
        model = Brewery
        fields = ('name','country','beers')

        name = forms.CharField()
        country = forms.CharField()
        beers = forms.CharField()


class BrewerySearchForm(forms.Form):
    class Meta:
        model = Brewery
        fields = ('name','country')



# country
class CountryCreateForm(forms.Form):
    class Meta:
        model = Country
        fields = ('name',)
        country = forms.CharField()

class CountrySearchForm(forms.Form):
    class Meta:
        model = Country
        fields = ('name',)



