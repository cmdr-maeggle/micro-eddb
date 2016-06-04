# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import ListView, TemplateView, DetailView

from µeddb.apps.resources.models import Resource
from µeddb.apps.ships.models import Ship
from µeddb.apps.engineers.models import Engineer, Blueprint

app_name = "engineers"

urlpatterns = [
    url(r"engineers^$", ListView.as_view(model=Engineer), name="index"),
    url(r"^blueprints$", ListView.as_view(model=Blueprint), name="blueprint_list"),
    url(r"^blueprints/(?P<pk>\d+)$", DetailView.as_view(model=Blueprint), name="blueprint_detail"),
]
