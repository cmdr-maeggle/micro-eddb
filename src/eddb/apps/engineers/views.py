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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        # add some more stuff
        engineer = self.object
        assert isinstance(engineer, Engineer)
        module_upgrades = (engineer.blueprints
                           .annotate(module_name=F("module_type__name"))
                           .values("module_name")
                           .annotate(grade_max=Max("grade"))
                           .order_by("grade_max", "module_name")
                           )
        context_data['module_upgrades'] = module_upgrades

        return context_data


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
