# Spatial Api

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c2a1e2da9504bce829df47519c62cf8)](https://app.codacy.com/app/taciogt/spatial-api?utm_source=github.com&utm_medium=referral&utm_content=taciogt/spatial-api&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/taciogt/spatial-api.svg?branch=master)](https://travis-ci.com/taciogt/spatial-api)

## Environment Setup

### Local Development


To start the application, run: `docker-compose up --build`

The API will be available at `localhost:80`

#### Local debugging

To run the python server in a local, the following dependencies should be installed:

OSX
```bin/bash
brew update
brew install geos
brew install gdal 
brew install proj
```


### Endpoints

#### Create PDV

#### Get PDV by ID

URI: `/point_of_sale/<pdv-id>`

Example of a valid request:
```json
Request URI: /point_of_sale/1

Response:
{
    "trading_name": "Adega Osasco",
    "owner_name": "Ze da Ambev",
    "document": "02453716000170",
    "address": {
        "x": -43.297337,
        "y": -23.013538
    }
}
Http Status Code: 200
```

Example of a request with an invalid id:
```json
Request URI: /point_of_sale/99999

Response:
Http Status Code: 404
```


#### Search PDV


### Assumptions
To develop this test, I made some assumptions about the business rules. 
If some of them are false, there are unit tests that facilitate refactorings.   
* The point of sale coverage area will always be a Multipolygon
* The point of sale address will always be a point.
* The JSON available as initial data for the system only contains Multipolygons with one polygon.
* Apenas os caracteres númericos do CNPJ são relevantes, os outros são apenas uma máscara
* In the point of sale document, only numeric characters are relevant. Characters such as "/" or "-" are considered as visualization mask. 
* The point of sale document won't have more than 25 characters. 






### Improvements:
* The API Server allows for it be available at any host. This is a configuration set at `backend/backend/settings.py` in `ALLOWED_HOSTS = ['*']`. It should be configured with only the expected host: the local development and the server's DNS.
* The application is running in debug mode on all environments. It should be configured by an environment variable to not run on debug mode on the cloud.


Useful links used during development:
* Tutorial for Django+Postgis: https://realpython.com/location-based-app-with-geodjango-tutorial/
* https://www.techiediaries.com/django-gis-geodjango/
* https://github.com/aws/amazon-ecs-cli/issues/318