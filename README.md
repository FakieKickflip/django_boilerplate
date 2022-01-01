
# DjangoBoilerplate for a fully functional development and production evironment for large web applications

<br>

## Table of Contents

- [What this project include](#projectinclude)
- [Development environment](#development)
- [Production environment](#production)
- [Docker commands](#contributing)

<br>

## With what this boilerplate project comes with

- Django Python web application
- Base templating
- Function based views
- Login system
- Registration system 
- Session based authentication
- Crispy forms
- Bootstrap 
- Postgres database
- Pre-defined models with relationships
- CRUD operations via form
- Query database via ORM 
- Async with jQeury
- Scheduled and background task with Django-Q
- Sending e-mails 
<br>

- Development and production environment 
- Dockerfile for dev and prod environment
- Docker-compose files for dev and prod environment
- Handle environment variables with .env files
- Nginx as reserved proxy to serve static files in production
- gunicorn as application server in production
<br>

- Full git control 

<br>
Use this as a basis and please customize your application as you like. 


<br>

## Development environment

The development environment should be used for improve the code and develope your application locally.
We are using the build in application server of Django. Do not use this in production.

Files which are related to the development environment:

- Dockerfile
- docker-compose.dev.yml
- entrypoint.sh
- env.dev

<br>

Commands for starting the development environment locally:

<code>docker-compose -f docker-compose.dev.yml build</code>

<code>docker-compose -f docker-compose.dev.yml up</code>



<br>
## Production evironment

The production environment comes with a nginx as web server and gunicorn for serving the application. 
Postgres is used as the database of choice. In sum there will be four containers. 

Files which are related to the production environment:

- Dockerfile.prod
- docker-compose.prod.yml
- entrypoint.prod.sh
- env.prod
- env.prod.db
- nginx/Dockerfile
- nginx/conf

<br>

Commands to start the production environment:

<code>docker-compose -f docker-compose.prod.yml build</code>

<code>docker-compose -f docker-compose.prod.yml up</code>

Migrate the models (only the first time and if you changed a model):

<code>docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput </code>

Collect all static files so that the nginx can serve them:

<code>docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear </code>
