#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Modules, Webpack and Tailwind set up
yarn
yarn run build
npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css

# Install modules 
python -m pip install --upgrade pip
pip install -r requirements.txt

# Collect Static
python manage.py collectstatic --no-input

# Migrate DB (Skipped for DEMO)
# python manage.py makemigrations
# python manage.py migrate
