## CI/CD

Render is a streamlined cloud hosting service for Your apps and websites. Render emerges as your one-stop solution, offering a unified cloud platform that simplifies your deployment and hosting experience. With Render, you can effortlessly launch and manage your apps and websites, leveraging a suite of powerful features designed to enhance your development workflow.

> Intro: What we offer

**Rocket Django** streamlines the deployment process, enabling you to effortlessly launch your applications on Render, a unified cloud platform designed for seamless deployment and hosting. With pre-configured scripts and a user-friendly interface, you can quickly get your Rocket Django application up and running without the hassle of manual configurations.


### Deploying Rocker Django on Render

Deploying Rocket Django on Render:

- Create a Render Account: Sign up for a free Render account to gain access to the unified cloud platform.

- Connect Your Git Repository: Link your Rocket Django Git repository to Render, enabling easy deployment from your codebase.

- Configure Deployment Settings: Utilize the pre-configured render.yaml file to define the deployment parameters for your Rocket Django application.

![Render web service configuration page](https://github.com/app-generator/rocket-django/assets/51070104/8db2e54a-f609-4149-ab0e-7d7051d8baff)

![Render web service configuration page](https://github.com/app-generator/rocket-django/assets/51070104/6ecc3ae2-2289-4000-aaa3-4a464f116973)

- Initiate Deployment: Trigger the deployment process with a single command, and Render will handle the rest, setting up and launching your application.

- Monitor and Manage: Access the Render dashboard to monitor your application's performance, manage resources, and make adjustments as needed.


### Understanding the deployment scripts

**Rocket Django** provides two scripts that aid the deployment of applications on Render.

Using `render.yaml` presents a way to deploy multiple services from one instance. It offers flexibility and a high level of customization.

`render.yaml` provides a blueprint of the application. This is the same configuration that can be done using Render's service configuration page as seen below:

Aside from `render.yaml`, Rocket Django also has the `build.sh` script which contains commands that set up and start the application.


### Understanding `render.yaml`

> How to use it

`render.yaml` defines the blueprint for your Rocket Django application's deployment, specifying the service type, environment, build commands, and environment variables.

```yaml
services:
  - type: web
    name: rocket-django
    plan: starter
    env: python
    region: frankfurt  # region should be the same as your database region.
    buildCommand: "./build.sh"
    startCommand: "gunicorn core.wsgi:application"
    envVars:
      - key: DEBUG
        value: False
      - key: SECRET_KEY
        generateValue: true
      - key: WEB_CONCURRENCY
        value: 4
```

This can be extended further, check [Render Blueprint Specification](https://render.com/docs/blueprint-spec) for more configuration options.


### Understanding `build.sh`
`build.sh` executes the necessary steps to prepare your application for deployment, including installing dependencies, collecting static assets, and running database migrations.

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

# Install & Execute WebPack 
npm i
npm run build

# Install modules 
python -m pip install --upgrade pip
pip install -r requirements.txt

# Collect Static
python manage.py collectstatic --no-input

# Migrate DB (Skipped for DEMO)
# python manage.py makemigrations
# python manage.py migrate
```

## Conclusion
**Rocket Django** simplifies the deployment process by providing ready scripts that can take your application from your local machine to a deployed application in seconds. These scripts can up updated to match your project needs.

## ✅ Resources
- 👉 [Render Blueprint Specification](https://render.com/docs/blueprint-spec) documentation
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**