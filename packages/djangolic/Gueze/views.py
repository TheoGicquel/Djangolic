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
    
    
    ic("filter")
    qs = Beer.objects.all()
    breweries = Brewery.objects.all()
    countries = Country.objects.all()
    ic(countries)
    ic(breweries)
    name_contains_query = request.GET.get('name')
    ibu_exact_query = request.GET.get('ibu')
    abv_exact_query = request.GET.get('abv')
    glass_exact_query = request.GET.get('glass')
    type_exact_query = request.GET.get('type')
    style_exact_query = request.GET.get('style')
    brewery_exact_query = request.GET.get('brewery')
    countries_sold_in_exact_query = request.GET.get('countries_sold_in')

    

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(name__icontains=name_contains_query)

    if is_valid_queryparam(ibu_exact_query):
        qs = qs.filter(ibu__exact=ibu_exact_query)

    if is_valid_queryparam(abv_exact_query):
        qs = qs.filter(abv__exact=abv_exact_query)
    
    if is_valid_queryparam(glass_exact_query):
        qs = qs.filter(glass__exact=glass_exact_query)
    
    if is_valid_queryparam(type_exact_query):
        qs = qs.filter(type__exact=type_exact_query)
    
    if is_valid_queryparam(style_exact_query):
        qs = qs.filter(style__exact=style_exact_query)
        
    if is_valid_queryparam(brewery_exact_query):
        qs = qs.filter(brewery__exact=brewery_exact_query)
    
    if is_valid_queryparam(countries_sold_in_exact_query):
        qs = qs.filter(countries_sold_in__exact=countries_sold_in_exact_query)
    
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