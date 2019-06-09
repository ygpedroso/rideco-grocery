# Contribution Guide:
[![framework: Django](https://img.shields.io/badge/framework-Django-006400.svg)](https://www.djangoproject.com/) [![framework: Graphene](https://img.shields.io/badge/framework-Graphene-ee7600.svg)](http://docs.graphene-python.org/projects/django/en/latest/)

## Prerequisites
1. `python3`, `pip`, `venv`

## Steps for running solution locally
1. Clone the repository `git clone git@github.com:ygpedroso/rideco-grocery.git`
2. Enter to the project folder `cd rideco-grocery/`
3. Create your virtualenv `python3 -m venv venv`, and activate it `source venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
5. Run application migrations `python3 manage.py migrate`
6. [OPTIONAL] Create a super user `python3 manage.py createsuperuser`
7. Run the application server `python3 manage.py runserver`
8. Test the GraphQL api in the `/api` endpoint

## Database configuration
By default the application will use an `sqlite3` database, but if the `DATABASE_URL` environment variable is provided then 
it will connect to this one instead. The `DATABASE_URL` environment variable must have this format: 
`postgres://USER:PASSWORD@HOST:PORT/NAME`. Currently it only supports `postgres` database. For using `mongodb` or `mysql` 
databases installing the `pip` packages for each driver is required.

## Tests
1. Run application Tests + coverage `python3 manage.py test`

## Debug
By default the application will obtain the `DEBUG` variable value from an environment variable. If it is not defined it
will fallback to `False` by default. To run the server with `DEBUG` enabled, provide the `DEBUG` environment variable with
`True`.   

## CORS
By default the server will not allow requests from different domain(only from `localhost:3000`), in order to override 
this behavior the `CORS_ORIGIN_ALLOW_ALL` environment variable needs to be set to `True` before running the server. Or
setting the `CORS_ORIGIN_ALLOWED_APP` to your app domain.

## Grocery List staging server url:
1. Base Url: [https://grocery-api.herokuapp.com/](https://grocery.herokuapp.com/)
2. GraphQL API(Enable endpoint and simple view for testing api): 
[https://grocery-api.herokuapp.com/api](https://grocery.herokuapp.com/api)