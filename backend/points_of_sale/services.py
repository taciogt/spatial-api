from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from points_of_sale.models import PointOfSale


def get_nearest_point_of_sale(lat, long):
    delivery_point = Point(lat, long)
    return PointOfSale.objects.filter(coverage_area__covers=delivery_point). \
        annotate(distance=Distance('address', delivery_point)). \
        order_by('distance').first()
