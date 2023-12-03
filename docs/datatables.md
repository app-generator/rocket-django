## DataTables

> Intro: What we offer

**Rocket Django** allows you to easily create data tables. Datatables makes it easier to perform operations like creating, reading, updating and deleting database table records.

Datatable can be accessed from the `DataTables` route under the `Apps` menu on the sidebar. Datatable gives you the ability to query the `Product` table and perform basic database operations on the same page.


## How it works

> Codebase: related app, model, template, js 

The DataTable feature is implemented using the `tables` application in the `apps` folder, and the user interface is rendered by `templates/apps/datatables.html`. To create a datatable, these are the steps to take:

- Create a form class in `apps/tables/forms.py` for the model to be rendered on the table. This form will be used in creating and updating database records. This is an example form for the `product` table:
```py
# apps/tables/forms.py
from django import forms
from apps.common.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            self.fields[field_name].widget.attrs['required'] = False
```
The model used to create the form was imported from `app/commons/models.py`. Model from any app can be used in the creation of datatables.

- Create view functions to handle the displaying the table, creating, deleting and updating entries in the database. This is done in `apps/tables/views.py`.
```py
# apps/tables/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.tables.forms import ProductForm
from apps.common.models import Product
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.tables.utils import product_filter


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


def post_request_handling(request, form):
    form.save()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = int(request.POST.get('price'))
        product.info = request.POST.get('info')
        product.save()
    return redirect(request.META.get('HTTP_REFERER'))
```
The `datatables` function handles the display of the table and creation of new entries in the database. The `post_request_handling` is used to save the database entry, and is called in the `datatables` function to save form data.

The `delete_product` and `update_product` functions are used to handle delete and update operations respectively.

- After creating the view functions, you will register them to their respective routes in `apps/tables/urls.py`.
```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.datatables, name="datatables"),
    path('delete-product/<int:id>/', views.delete_product, name="delete_product"),
    path('update-product/<int:id>/', views.update_product, name="update_product"),
]
```

- The data from the model, and the logic that handles creating, deleting and updating data from the user interface can be found in `templates/apps/datatables.html`.
```js
<script>
  fetch('/api/product/')
    .then(response => response.json())
    .then(data => {
      $('#products-body').DataTable({
        data: data,
        columns: [
          { title: 'ID', data: 'id' },
          { title: 'Name', data: 'name' },
          { title: 'Info', data: 'info' },
          { title: 'Price', data: 'price' },
          {
            title: 'Action',
            data: null,
            render: function (data, type, row) {
              return (
                `<button 
                class="edit-button" 
                id="updateProductButton" data-drawer-target="drawer-update-product-default" data-drawer-show="drawer-update-product-default" aria-controls="drawer-update-product-default" data-drawer-placement="right"
                type="button" 
                data-id="' + row.id + '"
              >
                <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                  <path d="M12.687 14.408a3.01 3.01 0 0 1-1.533.821l-3.566.713a3 3 0 0 1-3.53-3.53l.713-3.566a3.01 3.01 0 0 1 .821-1.533L10.905 2H2.167A2.169 2.169 0 0 0 0 4.167v11.666A2.169 2.169 0 0 0 2.167 18h11.666A2.169 2.169 0 0 0 16 15.833V11.1l-3.313 3.308Zm5.53-9.065.546-.546a2.518 2.518 0 0 0 0-3.56 2.576 2.576 0 0 0-3.559 0l-.547.547 3.56 3.56Z"/>
                  <path d="M13.243 3.2 7.359 9.081a.5.5 0 0 0-.136.256L6.51 12.9a.5.5 0 0 0 .59.59l3.566-.713a.5.5 0 0 0 .255-.136L16.8 6.757 13.243 3.2Z"/>
                </svg>
              </button>` +
                `<button class="delete-button ml-2" data-id="' + row.id + '">
                <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                  <path d="M17 4h-4V2a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v2H1a1 1 0 0 0 0 2h1v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6h1a1 1 0 1 0 0-2ZM7 2h4v2H7V2Zm1 14a1 1 0 1 1-2 0V8a1 1 0 0 1 2 0v8Zm4 0a1 1 0 0 1-2 0V8a1 1 0 0 1 2 0v8Z"/>
                </svg>
              </button>`);
            }
          },
        ]
      });

    })

</script>
```
The `fetch` function is used to query the API route that returns the products data from the database. This is then passed as the data to the datatable. This can be adapted to match whatever model you're working with.


![Rocket Django - Styled with Tailwind-Flowbite AppSeed - Datatable view](https://github.com/app-generator/dummy/assets/57325382/0ca99722-23e6-470f-8f9b-66544fb04ad0)

![Rocket Django - Styled with Tailwind-Flowbite AppSeed - Datatable create](https://github.com/app-generator/dummy/assets/57325382/95cbe45d-d421-406e-8ccc-4ee48654d133)

![Rocket Django - Styled with Tailwind-Flowbite AppSeed - Datatable update](https://github.com/app-generator/dummy/assets/57325382/e0f9b9f7-32df-4979-b3ef-75e63afc9d75)

![Rocket Django - Styled with Tailwind-Flowbite AppSeed - Datatable delete confirmation](https://github.com/app-generator/dummy/assets/57325382/f2bd6933-cdd1-46ad-96a2-e83bb65c85dd)


Datatables can be extended to match any data model, and simplifying the data creation and manipulation process.

## Conclusion
Rocket Django empowers you to seamlessly integrate DataTables into your applications, simplifying data viewing, creation, and manipulation. Datatables is an important feature of Rocket generator. It is easily customizable, and it can be extended as a template for other datatable creation.

## ✅ Resources
- 👉 [DataTables](https://datatables.net/extensions/scroller/examples/styling/jqueryui.html) documentation
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**
