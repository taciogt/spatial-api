from django.contrib.gis.db import models


class PointOfSale(models.Model):
    trading_name = models.CharField(max_length=100, null=False, blank=False)
    owner_name = models.CharField(max_length=100, null=False, blank=False)
    document = models.CharField(max_length=25, null=False, blank=False)
    coverage_area = models.MultiPolygonField()
    address = models.PointField()

    def to_dict(self):
        return {
            'trading_name': self.trading_name,
            'owner_name': self.owner_name,
            'document': self.document,
        }
