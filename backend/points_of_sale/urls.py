from django.urls import path, register_converter

from points_of_sale.views import PointsOfSaleView, NearestPointsOfSaleView


class FloatConverter:
    regex = '-?\d+(\.\d+)?'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return f'{value}'


register_converter(FloatConverter, 'float')


urlpatterns = [
    path('point_of_sale/<int:pk>', PointsOfSaleView.as_view(), name='get_point_of_sale_by_id'),
    path('point_of_sale', PointsOfSaleView.as_view(), name='create_point_of_sale'),
    path('point_of_sale/nearest/<float:lat>/<float:long>', NearestPointsOfSaleView.as_view(),
         name='get_nearest_point_of_sale')
]
