# sendEmail > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/',views.restaurantDetail, name='resDetailPage'),
    path('restaurantCreate/',views.restaurantCreate, name='resCreatePage'),
    path('restaurantCreate/create',views.Create_restaurant, name='resCreate'),
    path('categoryCreate/',views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create',views.Create_category, name='cateCreate'),
    path('categoryCreate/delete',views.Delete_category, name='cateDelete'),
]