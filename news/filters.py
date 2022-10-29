from django_filters import FilterSet
from .models import Category
from django.forms import DateTimeInput
import django_filters


class PostFilter(FilterSet):
    heading = django_filters.CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label='Heading'
    )

    category = django_filters.ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Select a category',
    )

    time_in = django_filters.DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        ),
    )




