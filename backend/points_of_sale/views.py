from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from points_of_sale.models import PointOfSale
import json


class PointsOfSaleView(View):
    def get(self, request, id):
        point_of_sale = PointOfSale.objects.get(id=id)

        return HttpResponse(json.dumps(point_of_sale.to_dict()), content_type='application/json')
