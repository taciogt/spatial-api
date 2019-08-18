from django.urls import path

from points_of_sale.views import PointsOfSaleView

urlpatterns = [
    path('point_of_sale/<int:id>', PointsOfSaleView.as_view(), name='get_point_of_sale_by_id'),
]
