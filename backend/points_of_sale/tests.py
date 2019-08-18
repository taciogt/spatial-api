from django.test import TestCase

from django.test import Client
from django.urls import reverse
from points_of_sale.models import PointOfSale
from django.contrib.gis.geos import Polygon, MultiPolygon, Point


class GetPointOfSaleByIdAPI(TestCase):
    def setUp(self):
        print('quantidade de pontos')
        print(PointOfSale.objects.count())
        pos_data = {
            'document': '12345',
            'owner_name': 'John',
            'trading_name': 'Doe',
            'coverage_area': MultiPolygon(Polygon((Point(0, 0), Point(1, 1), Point(0, 2), Point(0, 0)))),
            'address': Point(1, 0)
        }
        self.point_of_sale = PointOfSale(**pos_data)
        self.point_of_sale.save()

    def test_get_point_of_sale_by_valid_id(self):
        client = Client()
        url = reverse('get_point_of_sale_by_id', kwargs={'id': self.point_of_sale.id})
        print(url)
        response = client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data, {'trading_name': 'Doe', 'owner_name': 'John', 'document': '12345'})
        # self.fail()
