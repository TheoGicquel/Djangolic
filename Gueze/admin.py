from django.contrib import admin
from .models import Beer,Glass,Type,Style
# Register your models here.

@admin.register(Beer)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
    Beer._meta.get_fields()]
    
    
@admin.register(Glass)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
    Glass._meta.get_fields()]
    
@admin.register(Type)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
    Type._meta.get_fields()]
    
@admin.register(Style)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
    Style._meta.get_fields()]