# Python Flask API

This is a Restful API written in Python(Flask).

## Usage

A Make File is provided for convenienve:

 - **make compose** - creates and set up the containers
 - **make down** - stop containers
 - **make test** - run tests
 - **make drop** - drop the docker images
 - **make python** - go inside the python container
 - **make mongo** - go inside the mongo container

Or you can run the docker commands:

 - **docker-compose up -d** - creates and set up the containers
 - **docker exec python-api pytest -s** - run tests


## Endpoints
**Register** [POST]: /auth/register

Request body:

```json
{
    email: 'example@mail.com',
    firstName: 'Jonh',
    lastName: 'Doe',
    password: '123456'
}
```
Response body:

```json
{
    accessToken: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9',
}
```

**Login** [POST]: /auth/login

Request body:

```json
{
    email: 'example@mail.com',
    password: '123456'
}
```
Response body:

```json
{
    accessToken: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9',
}
```

**Get User Profile (me)** [POST]: /user/me

Request headers:

```json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
```
Response body:

```json
{
    email: 'example@mail.com',
    firstName: 'Jonh',
    lastName: 'Doe'
}
```

