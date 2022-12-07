from django.shortcuts import render
from .models import Beer,Style,Type,Glass,Country,Brewery
from .forms import BeerSearchForm, CountrySearchForm, BrewerySearchForm,CountryCreateForm,BeerCreateForm
from django.shortcuts import redirect
import random
from django.db.models import Q, Count
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




def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    print("--------- get -----------")
    print(request.GET.items)
    print("--------- /get -----------")
    
    qs = Beer.objects.all()
    breweries = Brewery.objects.all()
    name_contains_query = request.GET.get('name')
    ibu_exact_query = request.GET.get('ibu')
    abv_exact_query = request.GET.get('abv')
    glass_exact_query = request.GET.get('glass')
    type_exact_query = request.GET.get('type')
    style_exact_query = request.GET.get('style')
    brewery_exact_query = request.GET.get('brewery')

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(name__icontains=name_contains_query)

    elif is_valid_queryparam(ibu_exact_query):
        qs = qs.filter(ibu__exact=ibu_exact_query)

    elif is_valid_queryparam(abv_exact_query):
        qs = qs.filter(abv__exact=abv_exact_query)
    
    elif is_valid_queryparam(glass_exact_query):
        qs = qs.filter(glass__exact=glass_exact_query)
    
    elif is_valid_queryparam(type_exact_query):
        qs = qs.filter(type__exact=type_exact_query)
    
    elif is_valid_queryparam(style_exact_query):
        qs = qs.filter(style__exact=style_exact_query)

    return qs

def search_results_all(request):
    beers = Beer.objects.all()
    
    context = {
    "beers":beers,
    }
        
    return render(request, "beer/search-results.html",context)


def search_results(request):
    print('--------- search_results  -----------')

    if(request.method == "GET"):
        qs = filter(request)
        context = {
            'beers': qs
        }
        return render(request, "beer/search-results.html",context)

          
    elif(request.method == "POST" ):
        return render(request, "form/search.html")
        
    
    


def search_form_beer(request):
    print('--------- search_form_beer -----------')
    print("into form")
    context = {
        "BeerSearchForm": BeerSearchForm
    }

    
    return render(request, "forms/search.html",context)







def create_beer_form(request):
    print('--------- create_beer_form -----------')
    context = {
        "BeerCreateForm": BeerCreateForm
    }
    
    return render(request, "forms/create.html",context)


def create_beer_results(request):
    print('--------- create_beer_results -----------')
    print(request)
    print('--------- /post -----------')
    
    if(request.method == "POST"):
        form = BeerCreateForm(request.POST)
        if form.is_valid():
            id = form.instance.id
            print("--------- form -----------")
            print(form.clean)
            print("--------- form/ -----------")
            
            form.save()
            return redirect("beerview",id=id)
        else:
            return render(request, "forms/create.html",{"form":form})        
    
    return render(request, "error.html")

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

def beerview(request,id):

    #! This implementation is terrible right now, using primary keys to join would be better
    
    beer =  Beer.objects.get(id=id)
    
    return render(request, "beer/beer-view.html",context={"beer":beer})   


def beerview_all(request):
    
    #! might be dangerous to fetch all data like this, remove before production
    
    beers = Beer.objects.all()
    
    return render(request, "beer/search-results.html",context={"beers":beers})   