## Charts

**Rocket Django** empowers you to create interactive charts effortlessly using [Apexcharts](https://apexcharts.com/). Rocket Django simplifies integrating data from Django's ORM into Apexcharts, making it easier than ever to visualize your data.

The home page features a static line chart and several bar charts that can customized as you see fit.

![Rocket Django - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/7988e817-841d-4e88-8a10-726cad0ae3c7)

Under the App menu in the sidebar, you will see a new route called `Charts`. This page features a dynamic bar chart and pie chart utilizing data from the database.

![Rocket Django Charts Page - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/5b18f498-7cfc-4270-86f8-e77b2fb80e08)


## How it works

> Codebase: related app, model, template,  js

**Rocket Django** seamlessly integrates charts into your Django applications, maximizing modularity and reusability. Charts are treated as a separate Django application, ensuring flexibility and ease of customization.

Key Benefits:

- Modular Design: Charts are organized into a dedicated Django application, promoting code organization and making it easy to extend and reuse chart components. The chart application can be found in the `apps/charts` folder.

- Dynamic Data Visualization: Leverage models from other applications within your project to create charts that dynamically adapt to your data.

- Customized Chart Appearance: Customize the appearance and behaviour of your charts using the readily available template located at `templates/apps/charts.html`.

- Static Chart Creation: Create charts as static assets for use in specific pages or sections of your application. The homepage charts are a prime example, residing in `static/assets/charts.js`.


## ✅ Resources
- 👉 [ApexCharts](https://apexcharts.com/) official website
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**