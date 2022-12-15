from django.shortcuts import render
from .models import Beer,Style,Type,Glass,Country,Brewery
from .forms import BeerSearchForm, CountrySearchForm, BrewerySearchForm,CountryCreateForm,BeerCreateForm,BeerUpdateForm
from django.shortcuts import redirect
import random
from django.db.models import Q, Count
import os
from icecream import ic


s_app_name = "Gueze"
s_search_name = "Search Results"
s_create_name = "Create Beer"
s_about_name = "About"

s_res_name = "Results"
s_sep = " | "
s_search_title = s_app_name + s_sep + s_search_name
s_result_title = s_app_name + s_sep + s_res_name
s_create_title = s_app_name + s_sep + s_create_name
s_about_tile = s_app_name + s_sep + s_about_name

def get_editViewTitle(beer):
    return s_app_name + s_sep + "Editing " + beer.name

def get_beerviewTitle(beer):
    return s_app_name + s_sep + "View " + beer.name

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
    "title": s_result_title,
    }
        
    return render(request, "beer/search-results.html",context)


def search_results(request):
    

    if(request.method == "GET"):
        qs = filter(request)
        context = {
            "title": s_result_title,
            'beers': qs
        }
        return render(request, "beer/search-results.html",context)

          
    elif(request.method == "POST" ):
        return render(request, "form/search.html")
        
    
    


def search_form_beer(request):
    context = {
        "BeerSearchForm": BeerSearchForm,
        "title": s_search_title,
    }

    return render(request, "forms/search.html",context)


def edit_beer_form(request,beer_id):
    
    beer = Beer.objects.get(id=beer_id)
    context = {
        "BeerUpdateForm": BeerUpdateForm(instance=beer),
        "beer":beer,
        "title": get_editViewTitle(beer),
        
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
        "BeerCreateForm": BeerCreateForm,
        "title": s_create_title
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
    context = {
        "title": get_beerviewTitle(beer),
        "beer":beer
    }
    return render(request, "beer/beer-view.html",context)  


def about(request):
    context = {
        "title": s_about_tile
    }
    return render(request, "about/about.html",context)   

def beerview(request,id):
    beer =  Beer.objects.get(id=id)    
    context = {
        "title": get_beerviewTitle(beer),
        "beer":beer
    }
    return render(request, "beer/beer-view.html",context)   


def beerview_all(request):    
    beers = Beer.objects.all()
    context = {
        "title":"Gueze|index",
        "beer":beers
    }
    return render(request, "beer/search-results.html",context)   