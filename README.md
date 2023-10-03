<div align="center">
    <a href="https://github.com/app-generator/rocket-django">
        <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272178364-cbac6d97-b2dc-4d95-bab6-891f4ee7d84d.png"" width="64" height="64" alt="Rocket Icon">
    </a>
    <h1>
        <a href="https://github.com/app-generator/rocket-django">
            Rocket Django
        </a>
    </h1>
</div>

<div align="center">
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272187437-19b38cd4-f84f-451b-943a-e3f441d0e5d5.jpg" alt="Django Rocket - Open-source Starter styled with Tailwind and Flowbite.">
</div>

<br />

## Why Rocket Django

#### ***Supercharge your app instantly, launch faster, make $***

Login users, process payments and send emails at lightspeed. Spend your time building your startup, not integrating APIs. **Rocket Django** provides you with the boilerplate code you need to launch, FAST. 

#### ***Rocket your startup in days, not weeks*** 

The Django boilerplate with all you need to build your SaaS, AI tool, or any other web app. From idea to production in 5 minutes.

#### **48+ hours of headaches**

 - 1 hrs to setup the project 
 - 2 hrs integrate tooling
 - 2 hrs to handle Stripe
 - 1 hrs for Docker
 - 1 hr Google Oauth
 - ∞ hrs overthinking...
 - Quality [Support](https://appseed.us/support/) via `Email` & [Discord](https://discord.gg/fZC6hup) 

<br />

## Manual Build 

> Download code

```bash
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```
 
> Install **Django** modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> Install **Tailwind/Flowbite** (separate terminal)

```bash
$ cd static
$ yarn  
$ npx tailwindcss -i ./src/input.css -o ./dist/css/output.css --watch           
```

> Migrate DB

```
$ python manage.py makemigrations
$ python manage.py migrate
```

> Create Superuser & Start the APP

```
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

<br />

## Start With Docker

> Download code

```bash
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```

> Start with Docker Compose

```bash
$ docker-compose up --build 
``` 

Visit the app in the browser `localhost:5085`.

<br />

## Free vs. `PRO`

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                            | PRO - $499 (plus VAT)               | 🚀 Custom - $2999 (plus VAT)         |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ Django 4.2.x                        | **Everything in Free**, plus:         | **Everything in PRO**, plus:         |
| ✓ Best Practices                      | ✅ `OAuth` Google, GitHub             | ✅ **1mo Custom Development**        | 
| ✓ Extended User Model                 | ✅ **Stripe** Payments                | ✅ **Dedicated Developer**           |
| ✓ Celery                              | ✅ **Wagtail** CMS                    | ✅ Weekly Sprints                    |
| ✓ Charts                              | ✅ Multi-Language Support             | ✅ Technical SPECS                   |
| ✓ Docker                              | ✅ **Sentry** Error Reporting         | ✅ Documentation                     |
| ✓ [API Generator](https://github.com/app-generator/django-api-generator)       | ✅ Private REPO Access               | ✅ **30 days Delivery Warranty**     |
| ✓ CI/CD Flow via Render               | ✅ **Unlimited Projects**             | -                                     |
| ✓ Support via GitHub Issues           | ✅ Lifetime Updates                   | -                                     |
| -                                     | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/) | -      |
| -                                     | ✅ Deployment Assistance             | -                                     |
| ------------------------------------| ------------------------------------| ------------------------------------|
| -                                       | 🛒 `PRE Order`: **[$299](https://appseed.gumroad.com/l/rocket-django)** (via GUMROAD)         | 🛒 `Order`: **[$2999](https://appseed.gumroad.com/l/rocket-django-custom)** (via GUMROAD)              |   

<br />

## **Deploy on Render**

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on the `Update Existing Resources` button.
- Edit the Environment and [specify the PYTHON_VERSION](https://render.com/docs/python-version)
  - Version `3.11.5` was used for **[this deployment](https://rocket-django.onrender.com/)**
- After that, your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## License

@MIT

<br />

---
[Rocket Django](https://github.com/app-generator/rocket-django) - Open-source starter styled with Tailwind/Flowbite actively suported by **[AppSeed](https://appseed.us)**.
