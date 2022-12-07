"""djangolic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Gueze import views 
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('beers/', include('Gueze.urls')),
    
    path('beer/<int:beer_id>/', views.beerview, name="beerview"),
    path('index', views.index , name='index'),
    path('', views.index , name='index'),
    path('search', views.search_form_beer , name='search'),
    path('search/results/', views.search_results , name='search-results'),
    path('search/results/all/', views.search_results_all , name='search-results-all'),


    path('create', views.create_beer_form , name='create'),
    path('create/results/', views.create_beer_form , name='create_results'),
    
    path('update', views.update , name='update'),
    path('about', views.about , name='about'),
    path('beer',views.beerview,name="beerview"),
    path('beer/<int:id>/view', views.beerview, name="beerview"),
    path('beer/<int:id>/', views.beerview, name="beerview"),
    path('beer/all/', views.beerview_all, name="beerview"),
    path('random/',views.random_beer,name="random_beer")

]
