from django.contrib.auth.models import User
from .models import Medication
import django_filters


#para filtrar elementos que coinciden con la peticion 
class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Medication
        fields = ['name']