from django import forms
from django.forms import ModelForm
from .models import Beer, Glass, Country, Style, Type, Brewery
#! TODO : Try to add tailwind classes to forms
# beer
class BeerSearchForm(ModelForm.Form):
    class Meta:
        model = Beer
        fields = ('name','ibu','abv','glass','type','style','countries_sold_in','srm')


class BeerCreateForm(ModelForm.Form):
    class Meta:
        model = Beer
        fields = ('name', 'ibu', 'abv', 'glass', 'type', 'style', 'countries_sold_in', 'taste', 'image', 'srm')

        # Je sais plus exactement comment les mettre dans la bdd a regarder
        name = ModelForm.Charfield()
        ibu = ModelForm.Charfield()

        abv = ModelForm.Charfield()
        glass = ModelForm.Charfield()
        typeselect = ModelForm.Charfield()

        styleselect = ModelForm.Charfield()
        country = ModelForm.Charfield()
        tastedesc = ModelForm.Charfield()
        # A modifier pour les logo
        logo_icon = ModelForm.Charfield()
        logo_medium = ModelForm.Charfield()
        logo_large = ModelForm.Charfield()

        srm = ModelForm.Charfield()


# brewery

class BreweryCreateForm(ModelForm.Form):
    class Meta:
        model = Brewery
        fields = ('name','country','beers')

        name = ModelForm.Charfield()
        country = ModelForm.Charfield()
        beers = ModelForm.Charfield()


class BrewerySearchForm(ModelForm.Form):
    class Meta:
        model = Brewery
        fields = ('name','country')



# country
class CountryCreateForm(ModelForm.Form):
    class Meta:
        model = Country
        fields = ('name',)
        country = ModelForm.Charfield()

class CountrySearchForm(ModelForm.Form):
    class Meta:
        model = Country
        fields = ('name',)



