from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import *

def index(request):

  context = {
    'segment': 'dashboard',
  }
  return render(request, "dashboard/index.html", context)

@login_required(login_url='/users/signin/')
def starter(request):

  context = {}
  return render(request, "pages/starter.html", context)

def billing(request):
    context = { 'segment': 'billing' }
    return render(request, 'pages/billing.html', context)

def products(request):
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 10)
    products = paginator.get_page(page)
    context = {
        'segment': 'products',
        'products': products
    }
    return render(request, 'apps/datatables.html', context)
