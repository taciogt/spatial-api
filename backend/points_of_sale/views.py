import json

from django.http import HttpResponse, Http404
from django.views import View

from points_of_sale.models import PointOfSale


class PointsOfSaleView(View):
    def get(self, request, pk):
        try:
            point_of_sale = PointOfSale.objects.get(id=pk)
        except PointOfSale.DoesNotExist:
            raise Http404(f'Invalid PointOfSale id ({pk})')

        return HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')
