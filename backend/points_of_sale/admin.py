from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from points_of_sale.models import PointOfSale


@admin.register(PointOfSale)
class PointOfSaleAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
