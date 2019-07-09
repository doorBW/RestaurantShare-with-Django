from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html', content)
    
def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')
    
def restaurantCreate(request):
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')
    
def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    # return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("여기서 category Create 기능을 구현할거야.")