from django.urls import include,path
from . import views

urlpatterns = [
    #path('home/<param>/', views.home, name='home'),
path('', views.index , name='index'),
path('index', views.index , name='index'),

]