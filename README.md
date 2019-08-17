# Spatial Api

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