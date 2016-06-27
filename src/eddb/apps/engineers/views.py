# -*- coding: utf-8 -*-

from django.db.models import Max, F
from django.forms import CheckboxSelectMultiple
from django.views.generic import DetailView, ListView

import django_filters
from django_filters.views import FilterView

from eddb.apps.ships.models import ModuleType
from .models import Blueprint, BLUEPRINT_GRADE_CHOICES, Engineer


class EngineerDetailView(DetailView):
    model = Engineer


class EngineerListView(ListView):
    model = Engineer


class BlueprintFilter(django_filters.FilterSet):
    module_type = django_filters.ModelMultipleChoiceFilter(queryset=ModuleType.objects.all())
    grade = django_filters.MultipleChoiceFilter(widget=CheckboxSelectMultiple(), choices=BLUEPRINT_GRADE_CHOICES)

    class Meta(object):
        model = Blueprint
        fields = ["module_type", "grade"]


class BlueprintListView(FilterView):
    model = Blueprint
    filterset_class = BlueprintFilter
    template_name = "engineers/blueprint_list.html"
