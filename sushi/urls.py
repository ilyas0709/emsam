from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'sushi'


router = routers.DefaultRouter()
router.register(r'Category_list', CategoryListViewSet, basename='category-list')
router.register(r'Category_detail', CategoryAdminViewSet, basename='category-detail')
router.register(r'Food_list', FoodListViewSet, basename='food-list')
router.register(r'Food_detail', FoodAdminViewSet, basename='food-detail')
router.register(r'Portion_detail', PortionAdminView, basename='portion-detail')


urlpatterns = [
    path('', include(router.urls)),
]
