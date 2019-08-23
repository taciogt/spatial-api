# Spatial Api

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c2a1e2da9504bce829df47519c62cf8)](https://app.codacy.com/app/taciogt/spatial-api?utm_source=github.com&utm_medium=referral&utm_content=taciogt/spatial-api&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/taciogt/spatial-api.svg?branch=master)](https://travis-ci.com/taciogt/spatial-api)

## Environment Setup

### Local Development

To start the application, run: `docker-compose up --build`

The API will be available at `localhost:80`

#### Local debugging

To run the python server in the host, the following dependencies should be installed:

OSX
```bin/bash
brew update
brew install geos
brew install gdal 
brew install proj
```

There are steps necessary to prepare the system to run only the server in the host. 
It isn't implemented because the docker allows for development without debugging. 

## Endpoints

### Create PDV

URI: `/point_of_sale`

Example of a valid request:
```json
Request URI: /point_of_sale

Response:
{ 'tradingName': 'Bar One',
  'ownerName': 'Bar Owner ',
  'document': '122333',
  'address': '{ "type": "Point", "coordinates": [ 0.0, 2.0 ] }',
  'coverageArea': '{ "type": "MultiPolygon", "coordinates": [ [ [ [ 0.0, 0.0 ], [ 0.0, 3.0 ], [ 0.0, 6.0 ], [ 0.0, 0.0 ] ] ] ] }'
}
Http Status Code: 200
```

### Get PDV by ID

URI: `/point_of_sale/<pdv-id>`

Example of a valid request:
```json
Request URI: /point_of_sale/1

Response:
{
    "id": 1,
    "trading_name": "Adega Osasco",
    "owner_name": "Ze da Ambev",
    "document": "02453716000170",
    "address": "{ \"type\": \"Point\", \"coordinates\": [ -43.297337, -23.013538 ] }",
    "coverage_area": "{ \"type\": \"MultiPolygon\", \"coordinates\": [ [ [ [ -43.36556, -22.99669 ], [ -43.36539, -23.01928 ], [ -43.26583, -23.01802 ], [ -43.25724, -23.00649 ], [ -43.23355, -23.00127 ], [ -43.2381, -22.99716 ], [ -43.23866, -22.99649 ], [ -43.24063, -22.99756 ], [ -43.24634, -22.99736 ], [ -43.24677, -22.99606 ], [ -43.24067, -22.99381 ], [ -43.24886, -22.99121 ], [ -43.25617, -22.99456 ], [ -43.25625, -22.99203 ], [ -43.25346, -22.99065 ], [ -43.29599, -22.98283 ], [ -43.3262, -22.96481 ], [ -43.33427, -22.96402 ], [ -43.33616, -22.96829 ], [ -43.342, -22.98157 ], [ -43.34817, -22.97967 ], [ -43.35142, -22.98062 ], [ -43.3573, -22.98084 ], [ -43.36522, -22.98032 ], [ -43.36696, -22.98422 ], [ -43.36717, -22.98855 ], [ -43.36636, -22.99351 ], [ -43.36556, -22.99669 ] ] ] ] }"
}
Http Status Code: 200
```

Example of a request with an invalid id:
```json
Request URI: /point_of_sale/99999

Response:
Http Status Code: 404
```

### Search PDV

URI: `/point_of_sale/nearest/<latitude>/<longitude>`

Example of a valid request:
```json
Request URI: /point_of_sale/nearest/-43.297337/-23.013538

Response:
{
    "id": 1,
    "trading_name": "Adega Osasco",
    "owner_name": "Ze da Ambev",
    "document": "02453716000170",
    "address": "{ \"type\": \"Point\", \"coordinates\": [ -43.297337, -23.013538 ] }",
    "coverage_area": "{ \"type\": \"MultiPolygon\", \"coordinates\": [ [ [ [ -43.36556, -22.99669 ], [ -43.36539, -23.01928 ], [ -43.26583, -23.01802 ], [ -43.25724, -23.00649 ], [ -43.23355, -23.00127 ], [ -43.2381, -22.99716 ], [ -43.23866, -22.99649 ], [ -43.24063, -22.99756 ], [ -43.24634, -22.99736 ], [ -43.24677, -22.99606 ], [ -43.24067, -22.99381 ], [ -43.24886, -22.99121 ], [ -43.25617, -22.99456 ], [ -43.25625, -22.99203 ], [ -43.25346, -22.99065 ], [ -43.29599, -22.98283 ], [ -43.3262, -22.96481 ], [ -43.33427, -22.96402 ], [ -43.33616, -22.96829 ], [ -43.342, -22.98157 ], [ -43.34817, -22.97967 ], [ -43.35142, -22.98062 ], [ -43.3573, -22.98084 ], [ -43.36522, -22.98032 ], [ -43.36696, -22.98422 ], [ -43.36717, -22.98855 ], [ -43.36636, -22.99351 ], [ -43.36556, -22.99669 ] ] ] ] }"
}
Http Status Code: 200
```

Example of a request for a point without coverage:
```json
Request URI: /point_of_sale/nearest/19/13

Response is empty
Http Status Code: 204 
```

## Assumptions
To develop this test, I made some assumptions about the business rules. 
If some of them are false, there are unit tests that facilitate refactorings.   
*   The point of sale coverage area will always be a Multipolygon
*   The point of sale address will always be a point.
*   The JSON available as initial data for the system only contains Multipolygons with one polygon.
*   Apenas os caracteres númericos do CNPJ são relevantes, os outros são apenas uma máscara
*   In the point of sale document, only numeric characters are relevant. Characters such as "/" or "-" are considered as visualization mask. 
*   The point of sale document won't have more than 25 characters. 

## Improvements
*   The API Server allows for it be available at any host. This is a configuration set at `backend/backend/settings.py` in `ALLOWED_HOSTS = ['*']`. It should be configured with only the expected host: the local development and the server's DNS.
*   The application is running in debug mode on all environments. It should be configured by an environment variable to not run on debug mode on the cloud.
*   The CSRF protection was disabled to simplify the API. It should be correctly implemented to send to production.
*   Validate de document number (check if it is a valid CNPJ)
*   Generate a coverage report for the unit tests running on Travis. This report can be sent to Codacy with a badge showing the coverage percentage.


Useful links used during development:
*   Tutorial for Django+Postgis: https://realpython.com/location-based-app-with-geodjango-tutorial/
*   https://www.techiediaries.com/django-gis-geodjango/
*   https://github.com/aws/amazon-ecs-cli/issues/318