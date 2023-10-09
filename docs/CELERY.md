## Celery docs

- Install the dependencies
```bash
$ pip install -r requirements.txt
```

- In the base directory inside `tasks_scripts` folder you need to write your scripts file.
- Run the celery command from the CLI.
```bash
$ celery -A home worker -l info -B
```
- Run the django server
```bash
$ python manage.py runserver
```
- You will see a new route `Tasks` in the sidebar.
- You can start and cancel any task from the UI.