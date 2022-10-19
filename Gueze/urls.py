from django.urls import include,path
from Gueze import views


urlpatterns = [
    #path('home/<param>/', views.home, name='home'),
path('index/', views.index, name='index'),
]