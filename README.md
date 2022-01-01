
# DjangoBoilerplate for a fully functional development and production evironment for large web applications



## Table of Contents

- [What this project include](#projectinclude)
- [Development environment](#development)
- [Production environment](#production)
- [Docker commands](#contributing)


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

- Development and production environment 
- Dockerfile for dev and prod environment
- Docker-compose files for dev and prod environment
- Handle environment variables with .env files
- Nginx as reserved proxy to serve static files in production
- gunicorn as application server in production

- Full git control 



Download to your project directory, add `README.md`, and commit:

```sh
curl -LO http://git.io/Xy0Chg
git add README.md
git commit -m "Use README Boilerplate"
```


## Development environment

The development environment should be used for improve the code and develope your application locally.
We are using the build in application server of Django. Do not use this in production.

Files which are related to the development environment:

- Dockerfile
- docker-compose.dev.yml
- entrypoint.sh
- env.dev

Commands for starting the development environment locally:

“` docker-compose -f docker-compose.dev.yml build


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



