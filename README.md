# SofomoApp

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was created to meet the Python Developer recruitment requirements at Sofomo.
App is deployed on https://mg-sofomoapp.herokuapp.com and this repo contains dockerized app do run locally.

## Technologies
- API: Django framework with Django Rest Framework
- Database: Postgresql
- Nginx
- Gunicorn
- Swagger/Redoc
- Docker Compose
- heroku.com
- ipstack.com

## Setup

### Requirements
1. Docker

### Installation
1. Clone this repo
3. run 

        cd sofomoapp && decker-compose up --build
4. Use at http://localhost/

> **_NOTE:_**  Notice that App will start on port 80.

## Usage
1. To register your user use endpoint `account/api/register/` with POST method:
        
        {
            "username": "<string>",
            "password": "<string>",
            "first_name": "<string>",
            "last_name": "<string>"
        }

2. To get JWT Token use endpoint `auth/token/` with POST method:
        
        {
            "username": "<string>",
            "password": "<string>"
        }

 3. From now on add this header to all API requests:
        
        {"Authorization": "Bearer <your JWT Token>"}


## API Documentation:

- https://mg-sofomoapp.herokuapp.com/swagger/
- https://mg-sofomoapp.herokuapp.com/redoc/

### or (locally)

- http://localhost/swagger/
- http://localhost/redoc/

## TODO:
1. Add React Frontend (Started at frontend branch. I'm still React rookie).

## Source 

1. Registration endpoint inspired by:
https://medium.com/python-in-plain-english/django-rest-framework-jwt-auth-with-login-and-register-77f830cd8789

2. IP Geolocation service:
https://ipstack.com/

3. App deployed on:
https://heroku.com/