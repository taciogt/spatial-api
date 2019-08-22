# Spatial Api

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c2a1e2da9504bce829df47519c62cf8)](https://app.codacy.com/app/taciogt/spatial-api?utm_source=github.com&utm_medium=referral&utm_content=taciogt/spatial-api&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/taciogt/spatial-api.svg?branch=master)](https://travis-ci.com/taciogt/spatial-api)


### Endpoints



#### Create PDV
URI: `/point_of_sale/<pdv-id>`

#### Get PDV by ID
#### Search PDV


Hipóteses assumidas:
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