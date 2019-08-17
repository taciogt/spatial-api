from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from points_of_sale.models import PointOfSale


@admin.register(PointOfSale)
class PointOfSaleAdmin(OSMGeoAdmin):
    list_display = ('id', 'trading_name', 'owner_name')
