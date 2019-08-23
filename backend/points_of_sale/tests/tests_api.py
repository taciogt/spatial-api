from django.test import TestCase

from django.test import Client
from django.urls import reverse
from points_of_sale.models import PointOfSale
from django.contrib.gis.geos import Polygon, MultiPolygon, Point


class GetPointOfSaleByIdAPI(TestCase):
    def setUp(self):
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

        url = reverse('get_point_of_sale_by_id', kwargs={'pk': self.point_of_sale.id})

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data, {
            'id': self.point_of_sale.id,
            'trading_name': 'Doe',
            'owner_name': 'John',
            'document': '12345',
            'address': '{ "type": "Point", "coordinates": [ 1.0, 0.0 ] }',
            'coverage_area': '{ "type": "MultiPolygon", "coordinates": [ [ [ [ 0.0, 0.0 ], [ 1.0, 1.0 ], [ 0.0, 2.0 ],'
                             ' [ 0.0, 0.0 ] ] ] ] }'
        })

    def test_get_point_of_sale_by_invalid_id(self):
        client = Client()

        invalid_id = 999999
        url = reverse('get_point_of_sale_by_id', kwargs={'pk': invalid_id})

        response = client.get(url)
        self.assertEqual(response.status_code, 404)


class GetNearestPointOfSaleAPI(TestCase):
    def setUp(self):
        pos_data = {
            'document': '1',
            'owner_name': 'Owner 1',
            'trading_name': 'Trading 1',
            'coverage_area': MultiPolygon(Polygon((Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3), Point(0, 0)))),
            'address': Point(1, 1)
        }
        self.point_of_sale = PointOfSale(**pos_data)
        self.point_of_sale.save()

        self.point_of_sale_2 = PointOfSale(**{
            'document': '2',
            'owner_name': 'Owner 2',
            'trading_name': 'Trading 2',
            'coverage_area': MultiPolygon(
                Polygon((Point(0, 0), Point(-3, 0), Point(-3, -3), Point(0, -3), Point(0, 0)))),
            'address': Point(-1, -1)
        })
        self.point_of_sale_2.save()

    def test_get_nearest_point_of_sale_using_int(self):
        client = Client()

        url = reverse('get_nearest_point_of_sale', kwargs={'lat': 1, 'long': 1})

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['document'], '1')

    def test_get_nearest_point_of_sale_using_float(self):
        client = Client()

        url = reverse('get_nearest_point_of_sale', kwargs={'lat': 1.0, 'long': 1.0})

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['id'], self.point_of_sale.id)
        self.assertEqual(response_data['document'], '1')

    def test_get_nearest_point_of_sale_without_pos_available(self):
        client = Client()

        url = reverse('get_nearest_point_of_sale', kwargs={'lat': 999, 'long': 999})

        response = client.get(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b'')

    def test_get_nearest_point_of_sale_with_negative_coordinates(self):
        client = Client()

        url = reverse('get_nearest_point_of_sale', kwargs={'lat': -2, 'long': -1})

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['id'], self.point_of_sale_2.id)
        self.assertEqual(response_data['document'], '2')


class CreatePointOfSaleAPI(TestCase):
    def setUp(self):
        pos_data = {
            'document': '1',
            'owner_name': 'John',
            'trading_name': 'Doe',
            'coverage_area': MultiPolygon(Polygon((Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3), Point(0, 0)))),
            'address': Point(1, 1)
        }
        self.point_of_sale = PointOfSale(**pos_data)
        self.point_of_sale.save()

    def test_get_nearest_point_of_sale_using_int(self):
        client = Client()
        url = reverse('create_point_of_sale')

        data = {
            'tradingName': 'Bar One',
            'ownerName': 'Bar Owner ',
            'document': '122333',
            'address': '{ "type": "Point", "coordinates": [ 0.0, 2.0 ] }',
            'coverageArea': '{ "type": "MultiPolygon", "coordinates": [ [ [ [ 0.0, 0.0 ], [ 0.0, 3.0 ], [ 0.0, 6.0 ], '
                            '[ 0.0, 0.0 ] ] ] ] }'
        }

        # Act
        response = client.post(url, data=data)

        # Assert Response
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsNotNone(response_data['id'])
        self.assertEqual(response_data['document'], '122333')

        # Assert saved data
        point_of_sale = PointOfSale.objects.get(id=response_data['id'])
        self.assertEqual(point_of_sale.owner_name, data['ownerName'])
        self.assertEqual(point_of_sale.trading_name, data['tradingName'])
        self.assertEqual(point_of_sale.address.json, data['address'])
        self.assertEqual(point_of_sale.coverage_area.json, data['coverageArea'])
