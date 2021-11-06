from apps.apartments.models import ApartmentsModel

import django_filters as filters


class ApartmentFilter(filters.FilterSet):
    year_gt = filters.NumberFilter('price', 'gt')
    # park_name = filters.CharFilter('autopark', 'name__istartswith')

    class Meta:
        fields = ('price', 'year_gt',)
