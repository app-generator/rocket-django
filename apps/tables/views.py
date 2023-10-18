from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.tables.forms import ProductForm
from apps.common.models import Product
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.tables.utils import product_filter

# Create your views here.

def datatables(request):
  filters = product_filter(request)
  product_list = Product.objects.filter(**filters)
  form = ProductForm()

  page = request.GET.get('page', 1)
  paginator = Paginator(product_list, 5)
  products = paginator.page(page)

  if request.method == 'POST':
      form = ProductForm(request.POST)
      if form.is_valid():
          return post_request_handling(request, form)

  context = {
    'segment'  : 'datatables',
    'parent'   : 'apps',
    'form'     : form,
    'products' : products
  }
  
  return render(request, 'apps/datatables.html', context)



@login_required(login_url='/users/signin/')
def post_request_handling(request, form):
    form.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/signin/')
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = int(request.POST.get('price'))
        product.info = request.POST.get('info')
        product.save()
    return redirect(request.META.get('HTTP_REFERER'))