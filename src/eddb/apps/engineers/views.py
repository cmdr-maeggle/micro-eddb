# -*- coding: utf-8 -*-

import django_filters
from django_filters.views import FilterView
from django_filters.widgets import LinkWidget

from eddb.apps.ships.models import ModuleType
from .models import Blueprint


class BlueprintFilter(django_filters.FilterSet):
    module_type = django_filters.ModelMultipleChoiceFilter(queryset=ModuleType.objects.all(), widget=LinkWidget())
    # 'name'        : django_filters.CharFilter(lookup_expr='icontains'),
    grade = django_filters.NumberFilter(lookup_expr="lt")

    class Meta(object):
        model = Blueprint
        fields = ["module_type", "grade"]


class BlueprintsListView(FilterView):
    model = Blueprint
    filterset_class = BlueprintFilter
    template_name = "engineers/blueprint_list.html"
