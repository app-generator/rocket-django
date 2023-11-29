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

- To tell Celery where to find your Django settings, add `DJANGO_SETTINGS_MODULE` to your environmental variables. You can do this by opening a terminal window and running the following command:
```bash
$ export DJANGO_SETTINGS_MODULE=core.settings
```

To create your scripts, head over to the `tasks_scripts` folder within the base directory. Script files saved in this location can be executed using the `Async task manager` feature.

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

## Conclusion
The Asynchronous task handler feature makes it easy to run time-consuming tasks without affecting the user experience. This can be helpful for tasks like sending emails, processing payments, or generating reports.

Rocket Django utilizing celery serves as a valuable tool for streamlining task processes and improving the overall user experience in your web development projects.
