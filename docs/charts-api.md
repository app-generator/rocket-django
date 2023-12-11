## Charts API

**Rocket Django** empowers you to create interactive charts effortlessly using [Apexcharts](https://apexcharts.com/). Rocket Django simplifies integrating data from Django's res framework into Apexcharts, making it easier than ever to visualize your data.

The home page features a static line chart and several bar charts that can customized as you see fit.

![Rocket Django - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/7988e817-841d-4e88-8a10-726cad0ae3c7)


### Benefit of Rocket Django charts
**Rocket Django** seamlessly integrates charts into your Django applications, maximizing modularity and reusability. Charts are treated as a separate Django application, ensuring flexibility and ease of customization.

Key Benefits:

- Dynamic Data Visualization: Leverage models from other applications within your project to create charts that dynamically adapt to your data.

- Customized Chart Appearance: Customize the appearance and behaviour of your charts using the readily available template located at `templates/apps/charts.html`.

- Chart Creation using API data: Create charts using API data in specific pages or sections of your application. Static charts  `static/assets/charts.js`.


## How it works

> Codebase: related app, model, template,  js

Dynamic charts created in Rocket Django using API data are created in `static/assets/charts.js` and rendered on the page it is needed.

- Create the HTML element with the `id` property you want the chart created on, in this case, `products-bar-chart-api` and `products-pie-chart-api`
```html
<!-- templates/apps/charts.html-->
<!-- line 183-->
<div class="flex gap-5 items-center justify-between">
    <div class="w-full" id="products-bar-chart-api"></div>
    <div class="w-full" id="products-pie-chart-api"></div>
</div>
```

- The data for the chart is pulled and rendered on the HTML element targeting a specific `id`. This is done in `static/assets/charts.js` as seen below:
```js
// static/assets/charts.js
// line 481

if (document.getElementById('products-bar-chart-api')) {
    const apiUrl = '/api/product/';
    let dt = []

    const fetchData = async () => {
        try {
            const response = await fetch(apiUrl);
            const data = await response.json();
            dt = data
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
    await fetchData();
    
    const options = {
        colors: ['#1A56DB', '#FDBA8C'],
        series: [
            {
                name: 'Product',
                color: '#1A56DB',
                data: dt.map(product => ({ x: product.name, y: product.price }))
            },
        ],
        chart: {
            type: 'bar',
            height: '420px',
            fontFamily: 'Inter, sans-serif',
            foreColor: '#4B5563',
            toolbar: {
                show: false
            }
        },
        ...
    };

    const chart = new ApexCharts(document.getElementById('products-bar-chart-api'), options); 
    chart.render();
}

if (document.getElementById('products-pie-chart-api')) {
    const apiUrl = '/api/product/';
    let dt = []

    const fetchData = async () => {
        try {
            const response = await fetch(apiUrl);
            const data = await response.json();
            dt = data
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
    await fetchData();


    const chart = new ApexCharts(document.getElementById('products-pie-chart-api'), pieChartOptions(dt));
    chart.render();

    // init again when toggling dark mode
    document.addEventListener('dark-mode', function () {
        chart.updateOptions(pieChartOptions(dt));
    });
}
```
The `fecthData` function is used to get API data using JavaScript `fetch` API. The data from the `product` route is in the format:
```json
[
    {
        "id": 3,
        "name": "Adidas",
        "info": "Just another cool product",
        "price": 201
    },
    {
        "id": 4,
        "name": "Nike",
        "info": "This is a shoe shop",
        "price": 66
    },
    {
        "id": 5,
        "name": "Puma",
        "info": "Over priced Puma",
        "price": 666
    }
]
```

- The data from the API is added to the chart options for both charts and rendered.

Under the App menu in the sidebar, you will see a route called `Charts`. This page features a dynamic bar chart and pie chart under the `Charts via API` section that utilizes the product API data.

![Rocket Django Charts Page - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/26234f9f-ffdc-45ef-942e-f779a4bc6c50)

### Dashboard charts
Charts on the homepage are rendered using the `getMainChartOptions`, `getVisitorsChartOptions`, and `getSignupsChartOptions` functions in `static/assets/charts.js`. These functions use static data to create the charts as seen below:
```js
// static/assets/charts.js
const getMainChartOptions = () => {
    let mainChartColors = {}
    ...

    return {
        chart: {
            ...
        series: [
            {
                name: 'Revenue',
                data: [6356, 6218, 6156, 6526, 6356, 6256, 6056],
                color: '#1A56DB'
            },
            {
                name: 'Revenue (previous period)',
                data: [6556, 6725, 6424, 6356, 6586, 6756, 6616],
                color: '#FDBA8C'
            }
        ],
        ...
        xaxis: {
            categories: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
            ...
            },
        ...
        };
    }
}

if (document.getElementById('main-chart')) {
    const chart = new ApexCharts(document.getElementById('main-chart'), getMainChartOptions());
    chart.render();

    // init again when toggling dark mode
    document.addEventListener('dark-mode', function () {
        chart.updateOptions(getMainChartOptions());
    });
}

const getSignupsChartOptions = () => {
    let signupsChartColors = {}
    ...

    return {
        series: [{
            name: 'Users',
            data: [1334, 2435, 1753, 1328, 1155, 1632, 1336]
        }],
        labels: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
        chart: {
            type: 'bar',
            height: '140px',
            foreColor: '#4B5563',
            fontFamily: 'Inter, sans-serif',
            toolbar: {
                show: false
            }
        },
        ...
    };
}

if (document.getElementById('week-signups-chart')) {
    const chart = new ApexCharts(document.getElementById('week-signups-chart'), getSignupsChartOptions());
    chart.render();

    // init again when toggling dark mode
    document.addEventListener('dark-mode', function () {
        chart.updateOptions(getSignupsChartOptions());
    });
}
```
You can customize these functions to better align with the requirements of your specific application.


## Conclusion
**Rocket Django** provides an easy way to add charts to your application using API data, creating interactive dynamic charts. Harness the power of Rocket Django to create data-driven applications.


## ✅ Resources
- 👉 [ApexCharts](https://apexcharts.com/) official website
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**