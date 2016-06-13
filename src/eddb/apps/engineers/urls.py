# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import ListView, TemplateView, DetailView

from eddb.apps.engineers.views import BlueprintListView, EngineerDetailView, EngineerListView
from eddb.apps.resources.models import Resource
from eddb.apps.ships.models import Ship
from eddb.apps.engineers.models import Engineer, Blueprint

app_name = "engineers"

urlpatterns = [
    url(r"engineers$", EngineerListView.as_view(), name="engineer_list"),
    url(r"engineers/(?P<pk>\d+)$", EngineerDetailView.as_view(), name="engineer_detail"),
    url(r"^blueprints$", BlueprintListView.as_view(), name="blueprint_list"),
    url(r"^blueprints/(?P<pk>\d+)$", DetailView.as_view(model=Blueprint), name="blueprint_detail"),
]
