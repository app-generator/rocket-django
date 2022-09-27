# Rocket Django

Open-source **Django Generator and app customizer**. The project is basically an interface over the `AppSeed Service` with a few local codebase processing currently unsupported by the LIVE [App Generator](https://appseed.us/). 

> **STATUS**: `Under Development`

<br />

## Product Roadmap 

| Status | Action | CMD | Info | 
| --- | --- | --- | --- |
| ✅ | **Code basic structure** | `runner.py` (entry point) | - |
| ✅ | **Create a Django project** | `$ python runner.py create` | Create new project in `src` |
| ✅ | **Starts the project** | `$ python runner.py start` | Start on port `8000` |
| ❌ | **Add authentication** | `$ python runner.py auth` | `Not Implemented` |
| ❌ | **Use SQLite** | `$ python runner.py db sqlite` | `Not Implemented` |
| ❌ | **Use MySql** | `$ python runner.py db mysql` | `Not Implemented` |
| ❌ | **Docker** | `$ python runner.py docker add` | `Not Implemented` |
| ❌ | **Themes List** | `$ python runner.py themes` | `Not Implemented` |
| ❌ | **Theme Install** | `$ python runner.py theme volt` | `Not Implemented` |

<br />

## How to use it

> 👉 Download the code 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Create a new project

```bash
$ python runner.py create
```

<br />

> 👉 Start the project

```bash
$ python runner.py start 
```

<br />

![Rocket Django - Open-source generator for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/192149059-e79b141d-d596-44e0-880f-749842b757b1.png)

<br />

---
**Rocket Django** - Open-source generator for Django provided by **[App Generator](https://appseed.us/generator/)**.
