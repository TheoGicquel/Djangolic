from django import forms
from .models import Beer, Glass, Country, Style, Type, Brewery
#! TODO : Try to add tailwind classes to forms
# beer

class BeerSearchForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ('name', 'ibu', 'abv', 'glass', 'type', 'style', 'countries_sold_in', 'brewery')

        

class BeerCreateForm(forms.Form):
    class Meta:
        model = Beer
        fields = ('name', 'ibu', 'abv', 'glass', 'type', 'style', 'countries_sold_in', 'taste', 'image', 'srm')

        # Je sais plus exactement comment les mettre dans la bdd a regarder
        name = forms.CharField()
        ibu = forms.CharField()

        abv = forms.CharField()
        glass = forms.CharField()
        typeselect = forms.CharField()

        styleselect = forms.CharField()
        country = forms.CharField()
        tastedesc = forms.CharField()
        # image url field
        image = forms.CharField()

        srm = forms.CharField()


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



