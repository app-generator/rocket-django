from django.http import HttpResponse
from django.shortcuts import render
from apps.common.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'pages/apps/products.html', context)

