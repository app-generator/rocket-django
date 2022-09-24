# Rocket Django

Open-source Django generator and app customizer. The project is basically an interface over the AppSeed Service with a few local codebase processing currently unsupported by the LIVE App Generator. 

> Status: `UNSTABLE`, under development

<br />

> Product Roadmap 

| Status | Action | CMD | Info | 
| --- | --- | --- | --- |
| ✅ | **Code basic structure** | `runner.py` (entry point) | --- |
| ❌ | **Create a Django project** | `$ python runner.py create` | Generate a new project in `src` |
| ❌ | **Add authentication** | `$ python runner.py XXX` | @Todo |
| ❌ | **Use SQLite** | `$ python runner.py XXX` | @Todo |
| ❌ | **Use MySql** | `$ python runner.py XXX` | @Todo |
| ❌ | **Docker** | `$ python runner.py docker <add/remove>` | Default argument: `add` |
| ❌ | **Themes List** | `$ python runner.py themes` | List all available themes |
| ❌ | **Theme Install** | `$ python runner.py theme volt` | Install  |

<br />

## How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/rocket-django.git
$ cd rocket-django
```

<br />

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> Use the tool

```bash
$ python runner.py        # test command  
$ python runner.py <CMD>  # executes a subcommand  
```

<br />

---
Rocket Django - Open-source generator for Django provided by **[AppSeed Generator](https://appseed.us/generator/)**.
