from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class PointOfSale(models.Model):
    trading_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)