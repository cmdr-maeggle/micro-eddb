# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import ListView, DetailView

from eddb.apps.resources.models import Resource

app_name = "resources"

urlpatterns = [
    url(r"^$", ListView.as_view(model=Resource), name="index"),
    url(r"^resource/(?P<pk>\d+)$", DetailView.as_view(model=Resource), name="resource_detail"),
]
