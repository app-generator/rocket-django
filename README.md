<div align="center">
    <a href="https://rocket-django.onrender.com">
        <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272178364-cbac6d97-b2dc-4d95-bab6-891f4ee7d84d.png"" width="64" height="64" alt="Rocket Icon">
    </a>
    <h1>
        <a href="https://rocket-django.onrender.com">
            Rocket Django
        </a>
    </h1>
    <p>
        <strong>TailwindCSS</strong> &bull; <strong>Flowbite</strong> &bull; <strong>API (DRF)</strong> &bull; <strong>Celery Beat</strong> &bull; <strong>DataTables</strong> &bull; <strong>Charts</strong> &bull; <strong>Docker</strong> &bull; <strong>CI/CD</strong>
    </p>  
    <h3>
        <a href="https://docs.appseed.us/products/rocket/django/">
           📖 DOCS
        </a>
        &nbsp; &bull; &nbsp; 
        <a href="https://www.youtube.com/watch?v=rSFLcv00Bw8">
            Video
        </a>
        &nbsp; &bull; &nbsp;
        <a href="https://appseed.us/support/">
            Support 🚀
        </a>
    </h3>    
</div>

<br />

<div align="center">
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272299949-6f4a8fd7-7cce-472a-9566-9519db338c7d.gif" alt="Django Rocket - Open-source Starter styled with Tailwind and Flowbite.">
</div>

<br />

## Why [Rocket Django](https://github.com/app-generator/rocket-django)

#### ***Supercharge your app instantly, launch faster, make $***

Login users, process payments and send emails at lightspeed. Spend your time building your startup, not integrating APIs. **Rocket Django** provides you with the boilerplate code you need to launch, FAST. 

#### ***Rocket your startup in days, not weeks*** 

The Django boilerplate has all you need to build your SaaS, Analytics tool, or any other type of Web App. From idea to production in 5 minutes.

#### **48+ hours of headaches**

 - 1 hrs to setup the project 
 - 2 hrs integrate tooling
 - 2 hrs to handle Stripe
 - 1 hrs for Docker
 - 1 hr Google Oauth
 - ∞ hrs overthinking...
 - Free [Support](https://appseed.us/support/) via `Email` & [Discord](https://discord.gg/fZC6hup) 

<br />

## Manual Build 

> 👉 Download code

```bash
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```

> 👉 Create `.env` from `env.sample`

```env
DEBUG=False

SECRET_KEY=<STRONG_KEY_HERE>

# For Myql or PgSQL Persistence 
# DB_ENGINE=mysql
# DB_HOST=localhost
# DB_NAME=appseed_rocket_django
# DB_USERNAME=root
# DB_PASS=
# DB_PORT=3306

# SMTP configaration
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=
# EMAIL_HOST_PASSWORD=
```


> 👉 Install **Django** modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> 👉 Install **Tailwind/Flowbite** (separate terminal)

```bash
$ npm install
$ npm run dev        
```

> 👉 Migrate DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> 👉 `Create Superuser` & Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

<br />

## Free vs. `PRO`

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                            | PRO - 🛒 **[$499](https://appseed.gumroad.com/l/rocket-django)** | Enterprise - 🛒 **[$4,999](https://appseed.gumroad.com/l/rocket-django-enterprise)** |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ **Django 4.1.12**                                                 | **Everything in Free**, plus:                                                       | **Everything in PRO**, plus:          |
| ✓ Best Practices                                                    | ✅ **OAuth** `Google`, `GitHub`                                                     | ✅ **[CSV to Model Generator](https://www.youtube.com/watch?v=O6c76T3VYU8)**         | 
| ✓ **TailwindCSS**/`Flowbite`                                        | ✅ **Enhanced** [Charts](https://rocket-django-pro.onrender.com/charts/)            | ✅ **[CSV Data Loader](https://www.youtube.com/watch?v=O6c76T3VYU8)**                |
| ✓ Extended User Model                                               | ✅ **Enhanced** [DataTables](https://rocket-django-pro.onrender.com/tables/)        | ✅ **2 Weeks Custom Development**     |
| ✓ `Simple` [Charts](https://rocket-django.onrender.com/charts/)     | ✅ **[Media Files Manager](https://rocket-django-pro.onrender.com/file-manager/)**  | ✅ **1 Hour Video Call Presentation** |
| ✓ `Simple` [DataTables](https://rocket-django.onrender.com/tables/) | ✅ **Stripe** Payments                                                              | ✅ Dedicated Support                  |
| ✓ [API](https://rocket-django.onrender.com/api/product/) via `DRF`  | ✅ **Wagtail** CMS                                                                  | ✅ LIVE Deploy Assistance             |
| ✓ [Celery Beat](https://rocket-django.onrender.com/tasks/)          | ✅ **Multi-Language** (i18n) Support                                                | ✅ CI/CD for AWS, Azure, DO           |
| ✓ `Docker`                                                          | ✅ **Sentry** `Error Reporting`                                                     | -                                      |
| ✓ `CI/CD` Flow via Render                                           | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/)                 | -                                      |
| ✓ `Free Support` (GitHub Issues)                                    | ✅ `Unlimited Projects`                                                             | -                                      |
|  -                                                                  | ✅ `Private REPO Access`                                                            | -                                      |
|  -                                                                  | ✅ `Lifetime Updates`                                                               | -                                      |
| ------------------------------------| ------------------------------------| ------------------------------------|
| 🚀 [LIVE Demo](https://rocket-django.onrender.com/)                | 🚀 [LIVE Demo](https://rocket-django-pro.onrender.com/) | 🛒 `Order`: **[$4,999](https://appseed.gumroad.com/l/rocket-django-enterprise)** |   

<br />

## Start With Docker

> 👉 Download code

```bash
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```

> 👉 Start with Docker Compose

```bash
$ docker-compose up --build 
``` 

Visit the app in the browser `localhost:5085`.

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
[Rocket Django](https://github.com/app-generator/rocket-django) - Open-source starter styled with `Tailwind/Flowbite` actively supported by **[AppSeed](https://appseed.us)**.
