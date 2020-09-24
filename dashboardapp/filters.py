import django_filters
from .models import Datamodel

class dataFilter(django_filters.FilterSet):
    class Meta:
        model = Datamodel
        fields = ['name']
        