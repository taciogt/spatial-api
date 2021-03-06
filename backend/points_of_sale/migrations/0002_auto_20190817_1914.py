import json
import os

from django.db import connection
from django.db import migrations


def _get_file_path(filename):
    initial_data_directory = os.path.join(os.path.dirname(__file__), 'data')
    return os.path.join(initial_data_directory, filename)


def load_initial_data(apps, _):
    PointOfSale = apps.get_model('points_of_sale', 'PointOfSale')

    with open(_get_file_path('initial_data.json')) as file_data:
        data = json.load(file_data)
        for pos_data in data['pdvs']:
            document = ''.join([char for char in pos_data['document'] if char.isnumeric()])
            address = json.dumps(pos_data['address'])
            coverage_area = json.dumps(pos_data['coverageArea'])

            new_pos_data = {
                'id': pos_data['id'],
                'document': document,
                'trading_name': pos_data['tradingName'],
                'owner_name': pos_data['ownerName'],
                'address': address,
                'coverage_area': coverage_area,
            }
            point_of_sale, _ = PointOfSale.objects.get_or_create(**new_pos_data)
            point_of_sale.save()


def update_primary_key_auto_increment(apps, _):
    PointOfSale = apps.get_model('points_of_sale', 'PointOfSale')
    table_name = PointOfSale._meta.db_table
    with connection.cursor() as c:
        c.execute(f"SELECT setval('{table_name}_id_seq', (SELECT MAX(id) from \"{table_name}\"));")


class Migration(migrations.Migration):
    dependencies = [
        ('points_of_sale', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
        migrations.RunPython(update_primary_key_auto_increment),
    ]
