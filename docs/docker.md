## Docker

Step into a world where developing, sharing, and running your applications becomes a breeze. Docker, your open platform companion, empowers you to detach your applications from the complexities of your infrastructure, ensuring swift software delivery. No more waiting – Docker enables you to handle your infrastructure as seamlessly as your applications. Embrace Docker's user-friendly approach to shipping, testing, and deploying code, and witness a remarkable reduction in the time it takes to transition from coding to production.

Experience the magic of Docker as it helps you push updates to your users instantly, without worrying about downtime. With its responsive deployment and scaling capabilities, Docker lets you make the most out of your hardware, allowing you to effortlessly run more workloads with ease. Say goodbye to delays and hello to a smoother, more efficient application development journey.

> Intro: What we offer

**Rocket Django** can be tested and deployed using Docker containers. It contains the `Dockerfile` and `docker-compose.yml` which holds the configuration that allows the seamless creation of Docker containers and the deployment of Rocket Django.


### Understanding Docker configuration files

**Rocket Django** uses two configuration files to set up the Docker environment. These files are `Dockerfile` and `docker-compose.yml`, both found in the root directory of the project.

`docker-compose.yml` is a YAML file used to configure the application services. With a single command, this configuration is used to create applications with multiple parts. These are the configurations for Rocket Django:

```yaml
version: '3.8'
services:
  rocket-django:
    container_name: rocket_django
    restart: always
    build: .
    networks:
      - db_network
      - web_network
  nginx:
    container_name: nginx
    restart: always
    image: "nginx:latest"
    ports:
      - "5085:5085"
    volumes:
      - ./nginx:/etc/nginx/conf.d
    networks:
      - web_network
    depends_on: 
      - rocket-django
networks:
  db_network:
    driver: bridge
  web_network:
    driver: bridge
```

It defines a multi-container application with two services, `rocket-django` and `nginx`.

- `rocket-django` service:

    - container_name: This sets the container name to rocket_django.
    - restart: This tells Docker to automatically restart the container if it exits.
    - build: This instructs Docker to build the container image from the current directory (.).
    - networks: This specifies that the container should be connected to two networks: db_network and web_network.
    - depends_on: Indicates that the rocket-django container should be started before the nginx container, ensuring the application is ready before serving web traffic.

- `nginx` service:

    - container_name: This sets the container name to nginx.
    restart: Similar to rocket-django, this ensures automatic restarts.
    - image: Instead of building its image, this service uses the pre-built nginx:latest image.
    - ports: This maps the container port 5085 to the host port 5085. This means any request sent to your host on port 5085 will be forwarded to the container on port 5085.
    - volumes: This mounts thetainer_name: This sets the container name to nginx.
    restart: Similar to rocket-django, this ensures automatic restarts.
    - image: Instead of building its image, this service uses the pre-built nginx:latest image.
    - ports: This maps the container port 5085 to the host port 5085. This means any request sent to your host on port 5085 will be forwarded to the container on port 5085.
    - volumes: This mounts the local directory `./nginx` to the container's `/etc/nginx/conf.d` directory. This allows you to easily update your Nginx configuration without rebuilding the image.
    - networks: Same as rocket-django, this connects the container to web_network.
    - depends_on: This ensures the Nginx container only starts after the rocket-django container is up and running.

- `Networks`:

    - db_network: This defines a bridge network named db_network. This allows containers connected to this network to communicate with each other, potentially including a database server.
    - web_network: Another bridge network named web_network is used for communication between the nginx and rocket-django containers.

A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. This is the content of the `Dockerfile`:

```Dockerfile
FROM python:3.11.5

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install node 18 and npm
RUN set -uex; \
    apt-get update; \
    apt-get install -y ca-certificates curl gnupg; \
    mkdir -p /etc/apt/keyrings; \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
     | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg; \
    NODE_MAJOR=18; \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" \
     > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install nodejs -y;

# Install modules and webpack
RUN npm i
RUN npm run build

# Manage Assets & DB 
RUN python manage.py collectstatic --no-input 
RUN python manage.py makemigrations
RUN python manage.py migrate

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
```

This Dockerfile defines a multi-stage build for the Rocket Django application, consisting of three stages:

Stage 1 - Python environment setup:

- Starts with the python:3.11.5 image.
- Sets environment variables:
    - `PYTHONDONTWRITEBYTECODE`: Prevents writing bytecode for faster startup.
    - `PYTHONUNBUFFERED`: Disables output buffering for cleaner logs.
- Copies `requirements.txt` and installs Python dependencies with pip.
- Copies the entire application source code (.).

Stage 2 - Node.js environment setup:

- Sets environment variables for secure execution.
Updates and installs necessary packages like ca-certificates and curl.
- Sets up Node.js 18 installation:
- Downloads the GPG key for Node.js source.
- Adds the Node.js repository to the sources list.
- Updates and installs Node.js using apt-get.
- Installs frontend dependencies and builds the webpack assets.

Stage 3 - Application preparation and startup:

- Runs Django management commands:
    - `collectstatic` to gather static files.
    - `makemigrations` to create migrations for database schema changes.
    - `migrate` to apply the migrations to the database.
- Finally, defines the main command using `gunicorn`:
    - Specifies the `gunicorn-cfg.py` configuration file.
    - Starts the application using the `core.wsgi` entry point.

This multi-stage build separates the Python and Node.js environments for efficiency. It also streamlines the application setup and preparation for running in the container.


### Running Rocket Django using Docker

> How to use it 

To use the docker command, Docker must be installed on your machine. Follow the [installation guide](https://docs.docker.com/desktop/) if you don't have it. To start the Rocket Django application, run this command from the terminal in the same directory as the application:

```bash
$ docker compose up
```

It uses the configuration information in the `docker-compose.yml` file to pull the right images that would be used to build the application. After the images have been pulled, the commands in `Dockerfile` are executed and the application will get started. If you're building this application for the first time, this process might take a while to complete depending on your network speed.

Now, open http://127.0.0.1:5085 or http://localhost:5085 to see your app in action!

![Rocket Django - Styled with Tailwind-Flowbite AppSeed - Home page](https://github.com/app-generator/dummy/assets/57325382/d3d175ef-42e8-4d72-83e1-22acad6f6d88)

And that's it! Your app is up and running, ready to wow your users.


## Conclusion
**Rocket Django** is ready to deploy using Docker without any extra configuration. With Docker, the complexities of managing dependencies, environments, and infrastructure are abstracted, providing a consistent development and deployment experience.


## ✅ Resources
- 👉 [Docker](https://docs.docker.com/get-started/overview/) Overview
- 👉 [Dockerfile](https://docs.docker.com/engine/reference/builder/) Reference
- 👉 [Docker compose](https://docs.docker.com/compose/gettingstarted/) starter guide
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**