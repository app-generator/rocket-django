from django.shortcuts import render
from apps.pages.models import Product
from django.core import serializers


# Create your views here.

def index(request):
    products = serializers.serialize('json', Product.objects.all())
    context = {
        'segment'  : 'charts',
        'parent'   : 'apps',
        'products': products
    }
    return render(request, 'apps/charts.html', context)
