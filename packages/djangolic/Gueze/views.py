from django.shortcuts import render
from .models import Beer,Style,Type,Glass,Country,Brewery
from .forms import BeerSearchForm, CountrySearchForm, BrewerySearchForm,CountryCreateForm
from django.shortcuts import redirect
import random
import os

# Create your views here.
def index(request):
    context ={
        "title":"Gueze|index",
        "beercount":Beer.objects.count(),
        "stylecount":Style.objects.count(),
        "brewerycount": Brewery.objects.count(),
        
    }
    return render(request, "index.html",context)


def search_results_all(request):
    beers = Beer.objects.all()
    
    context = {
    "beers":beers,
    }
        
    return render(request, "beer/search-results.html",context)


def search_results(request):
    isValid = False
    if(request.method == "POST"):
        beerFormData = BeerSearchForm(request.POST)
        breweryFormData = BrewerySearchForm(request.POST)
        all_beers = Beer.objects.all()
        beers = all_beers
        form_name_field_value = request.POST.get('name')
        
        print("--------------------")
        print(form_name_field_value)
        print("--------------------")
        
        # get all beer with name
        for e in Beer.objects.all():
            if e.name != form_name_field_value:
                beers = beers.exclude(name=e.name)
        
        
        
        if(beerFormData.is_valid()):
          isValid = True
          pass
            
        if(breweryFormData.is_valid()):
          isValid = True
            
        context = {
            "beers":beers.values,
            "beerFormData":all_beers.values,
            "breweryFormData":""
        }
        if(isValid):
            return render(request, "beer/search-results.html",context)
        else:
            print(beerFormData.errors)
            return redirect(search_form)
    elif(request.method == "GET" ):
        return render(request, "forms/search.html")
    
    


def search_form(request):
    beer_form = BeerSearchForm
    country_form = CountrySearchForm
    brewery_from = BrewerySearchForm
    
    context = {
        "beer_form": beer_form,
        "country_form":country_form,
        "brewery_form":brewery_from
    }

    
    return render(request, "forms/search.html",context)

def create(request):
    form_country = CountryCreateForm
    
    return render(request, "forms/create.html")

def update(request):
    return render(request, "forms/update.html")

def delete(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    beer.delete()
    return render(request, "forms/delete.html")

def view(request, beer_id):
    return render(request, "beer/beer-view.html")   

def random_beer(request):
    beers = list(Beer.objects.all())
    beer = random.choice(beers)
    return render(request, "beer/beer-view.html",context={"beer":beer})  


def about(request):
    return render(request, "about/about.html")   

def beerview(request,beer_id):

    #! This implementation is terrible right now, using primary keys to join would be better
    
    beer =  Beer.objects.get(id=beer_id)
    
    return render(request, "beer/beer-view.html",context={"beer":beer})   


def beerview_all(request):
    
    #! might be dangerous to fetch all data like this, remove before production
    
    beers = Beer.objects.all()
    
    return render(request, "beer/search-results.html",context={"beers":beers})   