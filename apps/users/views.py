from django.http import HttpResponse
from django.shortcuts import render

from apps.common.models import Product

# Create your views here.

def index(request):

    prodName = ''
    
    if len( Product.objects.all() ):
        prodName = Product.objects.all()[0].name
        
    return HttpResponse("INDEX Users" + ' ' + prodName)
