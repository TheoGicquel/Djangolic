from django.urls import include,path
from Gueze.views import index


urlpatterns = [
    #path('home/<param>/', views.home, name='home'),
path('', index, name='index'),
]