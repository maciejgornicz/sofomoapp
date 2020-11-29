# SofomoApp

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was created to meet the Python Developer recruitment requirements at Sofomo.

## Technologies
- API: Django framework with Django Rest Framework
- Database: Postgresql
- Nginx
- Swagger/Redoc
- Docker Compose
- Heroku (deployed)

## Setup

### Requirements
1. Docker

### Installation
1. Clone this repo
3. run `cd sofomoapp && decker-compose up --build`
4. Use at http://localhost/

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
https://mg-sofomoapp.herokuapp.com/swagger/
https://mg-sofomoapp.herokuapp.com/redoc/
### or (locally)
http://localhost/swagger/
http://localhost/redoc/


