from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")
    
def restaurantDetail(request):
    return HttpResponse("restaurantDetail")
    
def restaurantCreate(request):
    return HttpResponse("restaurantCreate")
    
def categoryCreate(request):
    return HttpResponse("categoryCreate")