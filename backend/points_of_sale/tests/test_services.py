from django.contrib.gis.geos import Polygon, MultiPolygon, Point
from django.test import TestCase

from points_of_sale.models import PointOfSale
from points_of_sale.services import get_nearest_point_of_sale


class GetNearestPointOfSaleService(TestCase):
    def setUp(self):
        pos_data = {
            'document': '1',
            'owner_name': 'Owner One',
            'trading_name': 'Restaurant',
            'coverage_area': MultiPolygon(
                Polygon((Point(0, 0), Point(40, 0), Point(40, 40), Point(0, 40), Point(0, 0)))),
            'address': Point(5, 5)
        }
        self.point_of_sale = PointOfSale(**pos_data)
        self.point_of_sale.save()

        pos_data = {
            'document': '2',
            'owner_name': 'Owner Two',
            'trading_name': 'Bar',
            'coverage_area': MultiPolygon(
                Polygon((Point(10, 10), Point(50, 10), Point(50, 50), Point(10, 50), Point(10, 10)))),
            'address': Point(45, 45)
        }
        self.point_of_sale = PointOfSale(**pos_data)
        self.point_of_sale.save()

    def test_get_nearest_point_of_sale_without_coverage(self):
        point_of_sale = get_nearest_point_of_sale(99, 99)
        self.assertIsNone(point_of_sale)

    def test_get_nearest_point_of_sale_with_only_one_available(self):
        point_of_sale = get_nearest_point_of_sale(1, 1)
        self.assertEqual(point_of_sale.document, '1')

        point_of_sale = get_nearest_point_of_sale(46, 46)
        self.assertEqual(point_of_sale.document, '2')

    def test_get_nearest_point_of_sale_on_coverage_area_limit(self):
        point_of_sale = get_nearest_point_of_sale(0, 5)
        self.assertEqual(point_of_sale.document, '1')

    def test_get_nearest_point_of_sale_with_many_available(self):
        point_of_sale = get_nearest_point_of_sale(15, 15)
        self.assertEqual(point_of_sale.document, '1')

        point_of_sale = get_nearest_point_of_sale(35, 35)
        self.assertEqual(point_of_sale.document, '2')
