from django.shortcuts import render
from .models import Beer,Style,Type,Glass,Country,Brewery
from .forms import BeerSearchForm, CountrySearchForm, BrewerySearchForm,CountryCreateForm,BeerCreateForm,BeerUpdateForm
from django.shortcuts import redirect
import random
from django.db.models import Q, Count
import os
from icecream import ic

# Create your views here.
def index(request):
    context ={
        "title":"Gueze|index",
        "beercount":Beer.objects.count(),
        "stylecount":Style.objects.count(),
        "brewerycount": Brewery.objects.count(),
        
    }
    return render(request, "index.html",context)




def is_valid_queryparam(param):
    return param != '' and param is not None






def filter(request):
    qs = Beer.objects.all()

    # Use a dictionary to map query parameter names to filter criteria
    query_params = {
        'name': 'icontains',
        'ibu': 'exact',
        'abv': 'exact',
        'glass': 'exact',
        'type': 'exact',
        'style': 'exact',
        'brewery': 'exact',
        'countries_sold_in': 'exact'
    }

    # Iterate over the query parameters and apply the corresponding filter criteria
    for param, criteria in query_params.items():
        value = request.GET.get(param)
        if is_valid_queryparam(value):
            qs = qs.filter(**{f"{param}__{criteria}": value})

    return qs


def search_results_all(request):
    beers = Beer.objects.all()
    
    context = {
    "beers":beers,
    }
        
    return render(request, "beer/search-results.html",context)


def search_results(request):
    

    if(request.method == "GET"):
        qs = filter(request)
        context = {
            'beers': qs
        }
        return render(request, "beer/search-results.html",context)

          
    elif(request.method == "POST" ):
        return render(request, "form/search.html")
        
    
    


def search_form_beer(request):
    context = {
        "BeerSearchForm": BeerSearchForm
    }

    return render(request, "forms/search.html",context)


def edit_beer_form(request,beer_id):
    
    beer = Beer.objects.get(id=beer_id)
    context = {
        "BeerUpdateForm": BeerUpdateForm(instance=beer),
        "beer":beer,
        
    }
    
    return render(request, "forms/update.html",context)

def edit_beer_result(request,beer_id):
    beer = Beer.objects.get(id=beer_id)
    # edit beer in database
    if request.method == "POST":
        
        form = BeerUpdateForm(request.POST,instance=beer)
        if form.is_valid():
            form.save()
            beerpage = "/beer/" + str(beer.id) + "/view"
            return redirect(beerpage)
    else:
        form = BeerUpdateForm(instance=beer)
    return render(request, "forms/update.html", {"form": form})



def create_beer_form(request):
    
    context = {
        "BeerCreateForm": BeerCreateForm
    }
    
    return render(request, "forms/create.html",context)


def create_beer_results(request):
    
    
    # add beer to database
    
    if request.method == "POST":
        form = BeerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            beerpage = "/beer/" + str(Beer.objects.latest('id').id) + "/view"
            return redirect(beerpage)
    else:
        form = BeerCreateForm()
    return render(request, "forms/create.html", {"form": form})
    

def update(request):
    return render(request, "forms/update.html")

def beerdelete(request,beer_id):
    
    beer = Beer.objects.get(id=beer_id)
    
    beer.delete()
    return redirect("/random/")


def random_beer(request):
    beers = list(Beer.objects.all())

    # if no beers in database, return to index
    if not beers:
        return redirect("/")
    
    beer = random.choice(beers)
    return render(request, "beer/beer-view.html",context={"beer":beer})  


def about(request):
    return render(request, "about/about.html")   

def beerview(request,id):
    beer =  Beer.objects.get(id=id)    
    return render(request, "beer/beer-view.html",context={"beer":beer})   


def beerview_all(request):    
    beers = Beer.objects.all()
    return render(request, "beer/search-results.html",context={"beers":beers})   