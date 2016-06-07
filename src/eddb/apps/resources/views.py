# -*- coding: utf-8 -*-

from django.forms import CheckboxSelectMultiple, ValidationError
from django.views.generic import DetailView

import django_filters
from django_filters.views import FilterView

from .models import Resource, RESOURCE_GRADE_CHOICES, RESOURCE_TYPE_CHOICES



class ResourceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", min_length=3, max_length=100, help_text="no wildcard support atm")
    grade = django_filters.MultipleChoiceFilter(widget=CheckboxSelectMultiple(), choices=RESOURCE_GRADE_CHOICES)
    type = django_filters.MultipleChoiceFilter(widget=CheckboxSelectMultiple(), choices=RESOURCE_TYPE_CHOICES)

    class Meta(object):
        model = Resource
        fields = ["name", "type", "grade"]


class ResourceListView(FilterView):
    model = Resource
    filterset_class = ResourceFilter
    template_name = "resources/resource_list.html"


class ResourceDetailView(DetailView):
    model = Resource