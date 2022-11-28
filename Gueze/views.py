from django.shortcuts import render
from .models import Beer,Style,Type,Glass,Country,Brewery
from .forms import BeerSearchForm, CountrySearchForm, BrewerySearchForm,CountryCreateForm
import random
# Create your views here.
def index(request):
    return render(request, "index.html")




def search_results(request):
    if(request.method == "POST"):
        beercrit = BeerSearchForm(request.POST)
        brewerycrit = BrewerySearchForm(request.POST)
        beers = Beer.objects.all()
        if(beercrit.is_valid()):
            beercrit.save()
            beername = beercrit.cleaned_data["name"]
            beers = beers.filter(name__icontains=beername)
            beers = beers.filter(ibu__gte=beercrit.cleaned_data["ibu"])
            beers = beers.filter(abv__gte=beercrit.cleaned_data["abv"])
            beers = beers.filter(srm__gte=beercrit.cleaned_data["srm"])
            beers = beers.filter(glass__name=beercrit.cleaned_data["glass"])
            beers = beers.filter(type__name=beercrit.cleaned_data["type"])
            beers = beers.filter(style__name=beercrit.cleaned_data["style"])
            beers = beers.filter(countries_sold_in__name=beercrit.cleaned_data["countries_sold_in"])
        if(brewerycrit.is_valid()):
            brewerycrit.save()
            beers = beers.filter(brewery__name__icontains=brewerycrit.cleaned_data["name"])
            
        
        beers = Beer.objects.all()
        #beers = Beer.objects.filter(name__icontains=f_name)
        context = {
            "beers":beers,
            "beercrit":beercrit,
            "brewerycrit":brewerycrit
        }
        return render(request, "search-results.html",context)
    elif(request.method == "GET"):
        return render(request, "search.html")
    
    
    #return render(request, "search-results.html",{"styles":styles,"types":types ,"glass":glass})

def search_form(request):
    beer_form = BeerSearchForm
    country_form = CountrySearchForm
    brewery_from = BrewerySearchForm
    styles = Style.objects.all()
    types = Type.objects.all()
    glasses = Glass.objects.all()
    countries = Country.objects.all()
    breweries = Brewery.objects.all()
    
    context = {
        "styles":styles,
        "types":types,
        "glasses":glasses,
        "countries":countries,
        "breweries":breweries,
        "beer_form": beer_form,
        "country_form":country_form,
        "brewery_form":brewery_from
    }

    
    return render(request, "search.html",context)

def create(request):
    form_country = CountryCreateForm
    
    return render(request, "create.html")

def update(request):
    return render(request, "update.html")

def delete(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    beer.delete()
    return render(request, "delete.html")

def view(request, beer_id):
    return render(request, "view.html")   

def random_beer(request):
    beers = list(Beer.objects.all())
    beer = random.choice(beers)
    return render(request, "beer-view.html",context={"beer":beer})  


def about(request):
    return render(request, "about.html")   

def beerview(request,id):

    #! This implementation is terrible right now, using primary keys to join would be better
    
    beer =  Beer.objects.get(id=id)
    style = Style.objects.get(name=beer.style_name)
    type = Type.objects.get(name=beer.style_group)
    
    return render(request, "beer-view.html",context={"beer":beer,"style":style,"type":type})   


def beerview_all(request):
    
    #! might be dangerous to fetch all data like this, remove before production
    
    beers = Beer.objects.all()
    
    return render(request, "search-results.html",context={"beers":beers})   