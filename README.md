<div align="center">
    <a href="https://appseed.us/product/rocket/django/">
        <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272178364-cbac6d97-b2dc-4d95-bab6-891f4ee7d84d.png"" width="64" height="64" alt="Rocket Icon">
    </a>
    <h1>
        <a href="https://appseed.us/product/rocket/django/">
            Rocket Django
        </a>
    </h1>
    <p>
        <strong>TailwindCSS</strong> &bull; <strong>Flowbite</strong> &bull; <strong>API (DRF)</strong> &bull; <strong>Celery Beat</strong> &bull; <strong>DataTables</strong> &bull; <strong>Charts</strong> &bull; <strong>Docker</strong> &bull; <strong>CI/CD</strong>
    </p>  
    <h3>
        <a href="https://rocket-django.onrender.com/">
           Demo
        </a>
        &nbsp; &bull; &nbsp; 
        <a href="https://appseed.us/support/">
            Support
        </a>
        &nbsp; &bull; &nbsp;
        <a href="https://appseed.us/product/rocket-pro/django/">
            PRO Version 
        </a>
    </h3>    
</div>

<br />

<div align="center">
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272299949-6f4a8fd7-7cce-472a-9566-9519db338c7d.gif" alt="Django Rocket - Open-source Starter styled with Tailwind and Flowbite.">
</div>

<br />

## `Features`

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| [Free Version](https://appseed.us/product/rocket/django/)           | [PRO Version](https://appseed.us/product/rocket-pro/django/) | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ **Django 4.2.9**                                                   | **Everything in Free**, plus:                                                  | **Everything in PRO**, plus:         |
| ✓ **Best Practices**, `Modular Codebase`                             | ✅ **OAuth** `GitHub`                                                         | ✅ **1 Week** `Custom Development`  | 
| ✓ **TailwindCSS**/`Flowbite`                                         | ✅ **Media Files Manager**                                                    | ✅ **Team**: PM, Developer, Tester  |
| ✓ Extended User Model                                                | ✅ **React** / `ApexCharts`                                                   | ✅ Weekly Sprints                   |
| ✓ `Simple` [Charts](https://rocket-django.onrender.com/charts/)      | ✅ **Enhanced** [Charts](https://rocket-django-pro.onrender.com/charts/)      | ✅ Technical SPECS                  |
| ✓ `Simple` [DataTables](https://rocket-django.onrender.com/tables/)  | ✅ **Enhanced** [DataTables](https://rocket-django-pro.onrender.com/tables/)  | ✅ Documentation                    |
| ✓ [API](https://rocket-django.onrender.com/api/product/) via `DRF`   | ✅ **Multi-Language** (i18n)                                                  | ✅ **30 days Delivery Warranty**    |
| ✓ `Docker`                                                           | ✅ **Sentry** `Error Reporting`                                               | ✅ [CI/CD for AWS, DO](https://appseed.us/terms/#section-ci-cd) **(Extra)**    |
| ✓ `Free Support` (GitHub Issues)                                     | ✅ **[Celery](https://rocket-django.onrender.com/tasks/)** (async tasks)      |  -                                   |
| -                                                                    | ✅ **[Premium Support](https://appseed.us/support/)**                         |  -                                   |
| -                                                                    | ✅ `Unlimited Projects` & **SaaS**                                            |  -                                   |
| -                                                                    | ✅ `Private REPO Access`                                                      |  -                                   |
| -                                                                    | ✅ `Lifetime Updates`                                                         |  -                                   |
| ------------------------------------| ------------------------------------| ------------------------------------|
| ✓ [Rocket Demo](https://rocket-django.onrender.com/)                | 🚀 **[Rocket PRO Demo](https://rocket-django-pro.onrender.com/)** | 🛒 `Order`: **[$999](https://appseed.gumroad.com/l/rocket-package-week)** (GUMROAD) |   

<br />

## Why [Rocket Django](https://appseed.us/product/rocket/django/)

#### ***Supercharge your app instantly, launch faster, make $***

Login users, process payments and send emails at lightspeed. Spend your time building your startup, not integrating APIs. **Rocket Django** provides you with the boilerplate code you need to launch, FAST. 

#### ***Rocket your startup in days, not weeks*** 

The Django boilerplate has all you need to build your SaaS, Analytics tool, or any other type of Web App. From idea to production in 5 minutes.

#### **48+ hours of headaches**

 - 1 hrs to setup the project 
 - 2 hrs integrate tooling
 - 10 hr for coding Datatables
 - 5 hr for having thr Charts
 - 2 hrs for Docker
 - ∞ hrs overthinking...
 - Free [Support](https://appseed.us/support/) via `Email` & [Discord](https://discord.gg/fZC6hup) 

<br />

## Download Sources 

The product can be downloaded from the [official page](https://appseed.us/product/rocket/django/) or GitHub using GIT:

```bash
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```

Once the sources are available in the local filesystem, we can start the project using `Docker` or `manual build`. 

<br />

## Start with `Docker`

```bash
# Optional (kill all existing containers)
$ docker container kill $(docker ps -q) ; docker container rm $(docker ps -a -q) ; docker network prune -f 
# Start the APP
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running. The starter comes with two default users:

- Ordinary user: `test` / `test@appseed.us` / `Pass12__` (the password)
- Django SuperUser (admin): `admin` / `admin@appseed.us` / `Pass12__` (the password)

Once authenticated with the above credentials, the sidebar shows different items. 

<br />

## Manual Build 

> 👉 Create `.env` from `env.sample`

```env
DEBUG=False

SECRET_KEY=<STRONG_KEY_HERE>
```

> 👉 Install **Django** modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> 👉 Install **Tailwind/Flowbite** (another terminal)

Tested with **Node** `v18.20.0` (use at least this version or above)

```bash
$ npm install
$ npm run dev
$ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css --watch # DEVELOPMENT (LIVE reload)
$ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css         # PRODUCTION
```

> 👉 Migrate DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> 👉 `Create Superuser` & Start the [Rocket Django](https://appseed.us/product/rocket/django/) Starter

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, we can start using the starter.

<br />

## Use MySql 

By default, the starter uses SQLite for persistence. In order to use MySql, here are the steps: 

- Start the MySql Server
- Create a new DataBase
- Create a new user with full privileges over the database 
- Install the MySql Python Driver (used by Django to connect)
  - `$ pip install mysqlclient`
- Edit the `.env` with the SQL Driver Information & DB Credentials 

```env

DB_ENGINE=mysql
DB_HOST=localhost
DB_NAME=<DB_NAME_HERE>
DB_USERNAME=<DB_USER_HERE>
DB_PASS=<DB_PASS_HERE>
DB_PORT=3306

```

Once the above settings are done, run the migration & create tables: 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

## Production Build

To use the starter in production mode, here are the steps: 

- Set  **DEBUG=False** in `.env`
- Execute `collectstatic` command
  - `$ python manage.py collectstatic --no-input`

As a model, feel free to take a look at [build.sh](./build.sh), the file executed by the CI/CD flow for Render:   

<br />

## **Deploy on Render**

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect the `repo` that you want to deploy.
- Fill the `Service Group Name` and click on the `Update Existing Resources` button.
- Edit the Environment and [specify the PYTHON_VERSION](https://render.com/docs/python-version)
  - Version `3.11.5` was used for **[this deployment](https://rocket-django.onrender.com/)**
- After that, your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## Codebase 

```bash
< PROJECT ROOT >
   |
   |-- core/                 # Project Settings 
   |    |-- settings.py 
   |    |-- wsgi.py     
   |    |-- urls.py     
   |
   |-- home/                 # Presentation app 
   |    |-- views.py         # serve the HOMEpage  
   |    |-- urls.py     
   |    |-- models.py
   |
   |-- apps/                 # Utility Apps 
   |    |-- common/          # defines models & helpers
   |    |    |-- models.py   
   |    |    |-- util.py 
   |    |-- users            # Handles Authentication 
   |    |-- api              # DRF managed API
   |    |-- charts           # Showcase Different Charts
   |    |-- tables           # Implements DataTables
   |    |-- tasks            # Celery, async processing
   |
   |-- templates/            # UI templates 
   |-- static/               # Tailwind/Flowbite 
   |    |-- src/             # 
   |         |-- input.css   # CSS Styling
   |
   |-- Dockerfile            # Docker
   |-- docker-compose.yml    # Docker 
   |
   |-- render.yml            # CI/CD for Render
   |-- build.sh              # CI/CD for Render 
   |
   |-- manage.py             # Django Entry-Point
   |-- requirements.txt      # dependencies
   |-- .env                  # ENV File
   |
   |-- *************************************************      
```   

<br />

## License

@MIT

<br />

---
[Rocket Django](https://appseed.us/product/rocket/django/) - Open-source starter styled with `Tailwind/Flowbite` actively supported by **[AppSeed](https://appseed.us)**.
