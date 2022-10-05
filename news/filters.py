from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateTimeInput


class NewsFilter(FilterSet):
    time_in = DateTimeFilter(field_name='time_in',
                             lookup_expr='lte',
                             widget=DateTimeInput(format='%Y-%m-%dT%H:%M',
                                                  attrs={'type': 'datetime-local'}
                                                  )
                             ),

    class Meta:
        model = Post
        fields = {'heading': ['contains'],
                  'category': ['exact']
                  }

