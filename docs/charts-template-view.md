## Charts template view


**Rocket Django** empowers you to create interactive charts effortlessly using [Apexcharts](https://apexcharts.com/). Rocket Django simplifies integrating data from Django's ORM into Apexcharts, making it easier than ever to visualize your data.

Under the App menu in the sidebar, you will see a new route called `Charts`. This page features a dynamic bar chart and pie chart under the Charts (Template View) section utilizing data from the database.

![Rocket Django Charts Page - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/5b18f498-7cfc-4270-86f8-e77b2fb80e08)

### Benefit of Rocket Django charts
**Rocket Django** seamlessly integrates charts into your Django applications, maximizing modularity and reusability. Charts are treated as a separate Django application, ensuring flexibility and ease of customization.

Key Benefits:

- Modular Design: Charts are organized into a dedicated Django application, promoting code organization and making it easy to extend and reuse chart components. The chart application can be found in the `apps/charts` folder.

- Dynamic Data Visualization: Leverage models from other applications within your project to create charts that dynamically adapt to your data.

- Customized Chart Appearance: Customize the appearance and behaviour of your charts using the readily available template located at `templates/apps/charts.html`.


## How it works

> Codebase: related app, model, template,  js

Charts in Rocket Django can be created in the `charts` app and rendered as views, with model data sent as context to the template of the page. 

- To create a dynamic chart using the template view in Rocket Django, create the function to render the page in `apps/charts/views.py`. Model data that is used for the chart can be obtained by importing the model into the module used in creating the chart. Data from the `Product` model in `apps/common/models.py` is used to create the chart.
```py
# apps/charts/views.py
from django.shortcuts import render
from apps.common.models import Product
from django.core import serializers

def index(request):
    products = serializers.serialize('json', Product.objects.all())
    context = {
        'segment'  : 'charts',
        'parent'   : 'apps',
        'products': products
    }
    return render(request, 'apps/charts.html', context)
```
Model data is serialized into json format and passed with with the context dictionary. The data is serialized to make it easy to parse and render on the user interface.

- Add the path to the chart view just created to `apps/charts/urls.py` to make the chart accessible from the browser.
- For charts rendered using the API data, the elements are named `products-bar-chart-api` and `products-pie-chart-api`. The data for the chart is pulled and rendered using functions in `static/assets/charts.js`.

- Charts on the homepage are rendered using the `getMainChartOptions`, `getVisitorsChartOptions`, and `getSignupsChartOptions` functions. You can customize these functions to better align with the requirements of your specific application
```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="charts"),
]
```

- The chart is rendered using `templates/apps/charts.html`. The data from the context is parsed into a javascript object and used to render the bar chart and pie chart.
```html
// templates/apps/charts.html
// line 183
        <div class="flex gap-5 items-center justify-between">
          <div class="w-full" id="products-bar-chart"></div>
          <div class="w-full" id="products-pie-chart"></div>
        </div>

// line 271
<script>

  // Pull data from the backend
  const products = JSON.parse('{{ products | safe }}');

  function getProductsBarChart(data) {
    return {...}
  }
...
  const getProductsPieChart = (data) => {
    return {...}
  }

  (async () => {
    const productsBarChart = new ApexCharts(document.getElementById('products-bar-chart'), getProductsBarChart(products));
    productsBarChart.render();

    const productsPieChart = new ApexCharts(document.getElementById('products-pie-chart'), getProductsPieChart(products));
    productsPieChart.render();

    document.addEventListener('dark-mode', function () {
      productsPieChart.updateOptions(getProductsPieChart(products));
    });
  })();

</script>
```
The data from the context is parsed into a JavaScript object using the code:
```js
const products = JSON.parse('{{ products | safe }}');
```

The `getProductsBarChart` and `getProductsPieChart` functions are used to insert the data from the model to their respective charts, and then the data is rendered on the HTML element with the `products-bar-chart` and `products-pie-chart` IDs respectively. This can be altered to suit your use case and can also be extended to add other chart options.


## Conclusion
**Rocket Django** provides an easy way to add charts to your application using model and API data, creating interactive dynamic charts. Harness the power of Rocket Django to create data-driven applications.


## ✅ Resources
- 👉 [ApexCharts](https://apexcharts.com/) official website
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**