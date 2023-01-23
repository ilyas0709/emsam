from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'image', 'composition')
    list_display_links = ('id', 'category', 'name')
    search_fields = ('category', 'name')


class PortionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_food', 'price_size30', 'size36')
    list_display_links = ('id', 'get_food',)
    search_fields = ('get_food', 'price_size30')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Portion, PortionsAdmin)
# Register your models here.
