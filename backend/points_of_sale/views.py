import json

from django.http import HttpResponse, Http404
from django.views import View

from points_of_sale.models import PointOfSale
from points_of_sale.services import get_nearest_point_of_sale, create_point_of_sale


class PointsOfSaleView(View):
    def get(self, request, pk):
        try:
            point_of_sale = PointOfSale.objects.get(id=pk)
        except PointOfSale.DoesNotExist:
            raise Http404(f'Invalid PointOfSale id ({pk})')

        return HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')

    def post(self, request):
        trading_name = request.POST['tradingName']
        owner_name = request.POST['ownerName']
        document = request.POST['document']
        address = request.POST['address']
        coverage_area = request.POST['coverageArea']
        point_of_sale = create_point_of_sale(owner_name=owner_name, trading_name=trading_name, document=document,
                                             address=address, coverage_area=coverage_area)

        return HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')


class NearestPointsOfSaleView(View):
    def get(self, request, lat, long):
        point_of_sale = get_nearest_point_of_sale(lat=lat, long=long)
        if point_of_sale is not None:
            response = HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')
        else:
            response = HttpResponse(status=204)
        return response
