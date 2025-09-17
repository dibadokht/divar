from django.contrib import admin
from .models import City, Category , Ad

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id" , "name")
    search_fields = ("name",)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id" , "name")
    search_fields = ("name",)
    
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "city", "category")
    search_fields = ("title",)
    list_filter = ("city", "category")