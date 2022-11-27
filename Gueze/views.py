from django.shortcuts import render
from .models import Beer,Style,Type,Glass,Country,Brewery
from .forms import SearchBeerForm
import random
# Create your views here.
def index(request):
    return render(request, "index.html")




def search_results(request):
    if(request.method == "POST"):
        form = SearchBeerForm(request.POST)
        f_name = request.POST.get("name")
        f_ibu = request.POST.get("ibu")
        f_abv = request.POST.get("abv")
        
        beers = Beer.objects.filter(name__icontains=f_name)
        
        return render(request, "search-results.html",context={"beers":beers})
    elif(request.method == "GET"):
        return render(request, "search.html")
    
    
    #return render(request, "search-results.html",{"styles":styles,"types":types ,"glass":glass})

def search_form(request):
    form = SearchBeerForm
    styles = Style.objects.all()
    types = Type.objects.all()
    glasses = Glass.objects.all()
    countries = Country.objects.all()
    breweries = Brewery.objects.all()
    context = {"styles":styles,"types":types,"glasses":glasses,"countries":countries,"breweries":breweries,"form": form}
    return render(request, "search.html",context)

def create(request):
    return render(request, "create.html")

def update(request):
    return render(request, "update.html")

def delete(request):
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