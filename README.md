# Spatial Api

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c2a1e2da9504bce829df47519c62cf8)](https://app.codacy.com/app/taciogt/spatial-api?utm_source=github.com&utm_medium=referral&utm_content=taciogt/spatial-api&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/taciogt/spatial-api.svg?branch=master)](https://travis-ci.com/taciogt/spatial-api)

### Environment Setup

#### Local Development

To start the application, run: `docker-compose up --build`

The API will be available at `localhost:80`


### Endpoints

#### Create PDV
URI: `/point_of_sale/<pdv-id>`
Example of a valid request:
```json
Request:
/point_of_sale/1


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
Request:
/point_of_sale/99999


Response:
Http Status Code: 404
```

#### Get PDV by ID
#### Search PDV


### Assumptions
To develop this test, I made some assumptions about the business rules. If some of them are false, the  
* Área de cobertura sempre será um multipolígono
* Endereço sempre será um ponto
* O json com os pontos iniciais para popular a base de dados não contém nenhum Multipolígono com mais de um polígono
CNPJ
* O número máximo de número de um CNPJ é 25
* Apenas os caracteres númericos do CNPJ são relevantes, os outros são apenas uma máscara

Install dependencies:
Install GEOS:
MacOS
brew update
GEOS: brew install geos
GDAL: brew install gdal 
PROJ.4: brew install proj

Tutorial for Django+Postgis:
https://realpython.com/location-based-app-with-geodjango-tutorial/
Mac:
https://www.techiediaries.com/django-gis-geodjango/



https://github.com/aws/amazon-ecs-cli/issues/318


### Improvements:
* The API Server allows for it be available at any host. This is a configuration set at `backend/backend/settings.py` in `ALLOWED_HOSTS = ['*']`. It should be configured with only the expected host: the local development and the server's DNS.
* The application is running in debug mode on all environments. It should be configured by an environment variable to not run on debug mode on the cloud.