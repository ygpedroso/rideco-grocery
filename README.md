# Contribution Guide:

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

## Grocery List staging server url:
[https://rideco-grocery.herokuapp.com/](https://rideco-grocery.herokuapp.com/)