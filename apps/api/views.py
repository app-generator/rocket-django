from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.common.models import Product
from apps.api.forms import ProductForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.

def product_list(request):
    product_list = Product.objects.all()
    form = ProductForm()

    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 10)
    products = paginator.page(page)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return post_request_handling(request, form)

    context = {
        'products': products,
        'form': form
    }
    return render(request, 'pages/apps/products.html', context)



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