from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from points_of_sale.models import PointOfSale


def get_nearest_point_of_sale(lat, long):
    delivery_point = Point(lat, long)
    return PointOfSale.objects.filter(coverage_area__covers=delivery_point). \
        annotate(distance=Distance('address', delivery_point)). \
        order_by('distance').first()


def create_point_of_sale(owner_name, trading_name, document, address, coverage_area):
    point_of_sale = PointOfSale(owner_name=owner_name, trading_name=trading_name, document=document, address=address,
                                coverage_area=coverage_area)
    point_of_sale.save()
    return point_of_sale
