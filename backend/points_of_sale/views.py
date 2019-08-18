import json

from django.http import HttpResponse, Http404
from django.views import View

from points_of_sale.models import PointOfSale
from points_of_sale.services import get_nearest_point_of_sale


class PointsOfSaleView(View):
    def get(self, request, pk):
        try:
            point_of_sale = PointOfSale.objects.get(id=pk)
        except PointOfSale.DoesNotExist:
            raise Http404(f'Invalid PointOfSale id ({pk})')

        return HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')


class NearestPointsOfSaleView(View):
    def get(self, request, lat, long):
        point_of_sale = get_nearest_point_of_sale(lat=lat, long=long)
        if point_of_sale is not None:
            response = HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')
        else:
            response = HttpResponse(status=204)
        return response
