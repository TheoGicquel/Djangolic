from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    return render(request, "search.html")

def create(request):
    return render(request, "create.html")

def update(request):
    return render(request, "update.html")

def delete(request):
    return render(request, "delete.html")

def view(request, beer_id):
    return render(request, "view.html")   


def about(request):
    return render(request, "about.html")   

def beerview(request):
    return render(request, "beer-view.html")   