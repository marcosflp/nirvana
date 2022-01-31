## About

Nirvana challenge project


## Technical decisions

- Used this [django-boilerplate](https://github.com/marcosflp/django-boilerplate) project that I had created in the past to create the base for this project
- Choose to use GraphQL API because it's a great API client. Also, this django project already had it configured.
- Added the main business logic to `core/service/operation/`
- Added the main tests at `core/services/tests/test_operation.py`
- Added a mocked API at `core/integrations/api.py`
- Bonus: Coalescing configuration strategy can be configurable by changing the `strategy` param (more details in the "Using" section).


## Using

I deployed this project to Heroku. You can access it at https://nirvana-challenge.herokuapp.com/graphql

> With the local server running, access the endpoint http://localhost:8000/graphql to start making requests.

> To run the queries, copy and paste them into the right panel. Run one query at a time

#### Get coalesced AVERAGE operations

```gql
query {
  getOperations(filters: {
    memberId: "1", 
    strategy: "AVERAGE"
  }) {
    strategy
    deductible
    stopLoss
    oopMax
  }
}
```

#### Get coalesced COUNT operations

```gql
query {
  getOperations(filters: {
    memberId: "1", 
    strategy: "COUNT"
  }) {
    strategy
    deductible
    stopLoss
    oopMax
  }
}
```

#### Get coalesced MAX operations

```gql
query {
  getOperations(filters: {
    memberId: "1", 
    strategy: "MAX"
  }) {
    strategy
    deductible
    stopLoss
    oopMax
  }
}
```

#### Get coalesced MIN operations

```gql
query {
  getOperations(filters: {
    memberId: "1", 
    strategy: "MIN"
  }) {
    strategy
    deductible
    stopLoss
    oopMax
  }
}
```

#### Get coalesced SUM operations

```gql
query {
  getOperations(filters: {
    memberId: "1", 
    strategy: "SUM"
  }) {
    strategy
    deductible
    stopLoss
    oopMax
  }
}
```


## Setup

Clone the project
```shell
$ git clone git@github.com:marcosflp/nirvana.git
$ cd nirvana
```

Install pre-commit
```shell
$ pip install pre-commit
$ pre-commit install
```

### Docker

- Running the app: `$ docker compose up`
- Running tests: `docker compose exec web pytest`

### Locally

- Create a new virtual env
- Install the dependencies: `$ pip install -r requirements.txt`
- You have to install and run the postgres server. Also, configure the database settings 
- Run migrations: `$ python manage.py migrate`
- Running the server: `$ python manage.py runserver`
- Running tests: `$ pytest`


## Deployment

Automatically deploy this project to Heroku!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### How it works

The "Deploy to Heroku" button enables users to deploy apps to Heroku without leaving the web browser, and with little or no configuration. There are four conf files required to deploy this project: 

#### `app.json`

This file describes the settings to automatically deploy the project to Heroku.

- **env**: environment variables. Most of the settings is already configured. You just need to make sure to set the `ALLOWED_HOSTS` and `FRONTEND_APP_URL` correctly to avoid CORS problems 
- **addons**: specify the services used by the application (e.g.: postgres)
- **formation**: define the dyno instances. You can set the size and the amount of instances
- **buildpacks**: specify how to build the application. By adding `"heroku/python"` heroku will automatically:
  - Build a python instance to run the project
  - Install the project's dependencies from the `requirements.txt` file
  - Run `python manage.py collectstatic`

#### `Procfile`

This file specifies the commands that are executed by the app on startup. We are using it to run the django and celery after Heroku finishes the deployment.

#### `bin/post_compile`

This is a bash script file that is used by `"heroku/python"` build-pack to run commands at the end of the deployment cycle.

We are using this file to automatically run the migrations.

#### `runtime.txt`

Specify the python version to be used by `"heroku/python"` build-pack
