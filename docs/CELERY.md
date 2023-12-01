## Celery docs

### Celery introduction
Celery is a tool that helps you manage tasks in the background, independent of the main application's workflow. Celery is a tool that helps you run time-consuming tasks without slowing down your application or making it unresponsive. Celery allows you to distribute tasks/jobs across several threads.

**Rocket Django** offers the `Async task manager` feature, which makes use of Celery to run scripts in the background without affecting the main application's performance. This is done by placing the scripts in a task queue, which Celery then manages and executes. This allows users to run time-consuming tasks without having to wait for them to finish before continuing with other tasks.

### Requirements
Celery needs a way to send and receive messages, so you'll need to install a message broker like RabbitMQ or Redis.

**Rocket Django** is pre-configured to utilize Redis as its message broker, but you have the flexibility to switch to your preferred broker if needed.

### Installation and setup
- Install the dependencies
```bash
$ pip install -r requirements.txt
$ npm install
```

- Copy the `env.sample` file and name it `.env`. You can do this using the following command in your command line
```bash
$ cp env.sample .env
```

- Inside the `.env file`, create the variable `CELERY_BROKER`. If you are using Redis running on your computer, the value of `CELERY_BROKER` should be:
```sh
#.env
...
CELERY_BROKER="redis://localhost:6379"
``` 

- To tell Celery where to find your Django settings, add `DJANGO_SETTINGS_MODULE` to your environmental variables. You can do this by opening a terminal window and running the following command:
```bash
$ export DJANGO_SETTINGS_MODULE=core.settings
```

- The Celery configuration file, named `celery.py`, defines how Celery will operate within your Django project. It is located in your `home` directory.
```py
# home/celery.py
...
if os.environ.get('DJANGO_SETTINGS_MODULE'):

    app = Celery('core')

    # - namespace='CELERY' means all celery-related configuration keys should have a `CELERY_` prefix.
    app.config_from_object('django.conf:settings', namespace='CELERY')

    # Load task modules from all registered Django apps.
    app.autodiscover_tasks()
``` 

- The configuration options for celery can be found in `core/settings.py`. More configuration options can be found in Celery's [documentation](https://docs.celeryq.dev/en/stable/userguide/configuration.html)
```py
CELERY_SCRIPTS_DIR        = os.path.join(BASE_DIR, "tasks_scripts" )

CELERY_LOGS_URL           = "/tasks_logs/"
CELERY_LOGS_DIR           = os.path.join(BASE_DIR, "tasks_logs"    )

CELERY_BROKER_URL         = os.environ.get("CELERY_BROKER", "redis://localhost:6379")
CELERY_RESULT_BACKEND     = os.environ.get("CELERY_BROKER", "redis://localhost:6379")

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT    = 30 * 60
CELERY_CACHE_BACKEND      = "django-cache"
CELERY_RESULT_BACKEND     = "django-db"
CELERY_RESULT_EXTENDED    = True
CELERY_RESULT_EXPIRES     = 60*60*24*30 # Results expire after 1 month
CELERY_ACCEPT_CONTENT     = ["json"]
CELERY_TASK_SERIALIZER    = 'json'
CELERY_RESULT_SERIALIZER  = 'json'
```

To create your scripts, head over to the `tasks_scripts` folder within the base directory. Script files saved in this location can be executed using the `Async task manager` feature.

- In the root folder of the application, create a folder called `task_logs`. You can do that from the terminal using the command:
```bash
$ mkdir tasks_logs
```

- Run the celery command from the terminal
```bash
$ celery -A home worker -l info -B
```

- Run node server to allow the use of tailwind on another terminal
```bash
$ npm run dev
```

- Run the Django server on a different terminal
```bash
$ python manage.py runserver
```

Visit https://localhost:8000 to view the application.

![Rocket Django - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/409d6211-d1ed-4be0-8fca-d5ea58693481)

- Under the App menu in the sidebar, you will see a new route called `Tasks`.

![Rocket Django Tasks Page - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/d3b2ae6b-6971-4005-aec4-7aa95c7eac5a)

- You can start and cancel any task from the UI that exists as a script in the `tasks_scripts` folder.

### Adding a new script
Django Celery allows you to create custom scripts that can be executed from the user interface (UI). These scripts can perform various tasks, such as backups, data processing, or sending emails.

- The first step is to locate the `tasks_scripts` directory within your project's base directory. This directory is where custom Celery scripts should be placed.

- Inside the `tasks_scripts` directory, create a new Python file. In this tutorial, we'll use the filename `backup_db.py`.
```py
# task_scripts/backup_db.py
import os, shutil
from datetime import datetime

def main():
    try:
        DB_LOCATION = "db.sqlite3"

        BACKUP_NAME = f"db_backup_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.sqlite3"

        print(BACKUP_NAME)

        if not os.path.exists("db_backup"):
            os.mkdir("db_backup")

        shutil.copyfile(DB_LOCATION, "db_backup/" + BACKUP_NAME)

        exit(0)
    except Exception as e:
        print( 'Err: ' + str( e ) )
        exit(1)

if __name__ == "__main__":
    main()
```

This script creates a backup of the current database in use by creating a copy of the database. Once you have added this script to the `tasks_scripts` folder, it can be executed from the application.

### Adding a new task
Tasks to be executed by Celery can be added from the user interface of the application.

- Navigate to the `Tasks` section of the application. You can access it from the `Apps` menu on the sidebar.

- The scripts located in the `tasks_scripts` folder are already preloaded and ready to be executed.

- To execute tasks, you need to be logged in as an administrator. However, anyone can view the progress of tasks in execution.

![Rocket Django Tasks Page - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/aad832d4-ff62-44a1-a973-23c42e13acd8)

On the tasks page, you can select and execute the desired tasks. The status of the last executed task and a history of previously executed tasks are displayed for your reference.

![Rocket Django Tasks Page - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/cada9eb2-93ec-4f9c-85be-163798060471)

## Conclusion
The Asynchronous task handler feature makes it easy to run time-consuming tasks without affecting the user experience. This can be helpful for tasks like sending emails, processing payments, or generating reports.

Rocket Django utilizing celery serves as a valuable tool for streamlining task processes and improving the overall user experience in your web development projects.

## ✅ Resources
- 👉 [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) official documentation
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**
