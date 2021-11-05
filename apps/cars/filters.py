from apps.cars.models import CarModel

import django_filters as filters


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter('year', 'gt')
    park_name = filters.CharFilter('autopark', 'name__istartswith')

    class Meta:
        fields = ('year', 'model', 'year_gt', 'park_name')
