from django.contrib import admin
from .models import Beer, Glass, Country, Style, Type, Brewery
# Register your models here.

admin.site.register(Beer)
admin.site.register(Glass)
admin.site.register(Type)
admin.site.register(Style)
admin.site.register(Country)
admin.site.register(Brewery)
