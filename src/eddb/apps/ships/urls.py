# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import ListView

from eddb.apps.ships.models import Ship

app_name = "ships"

urlpatterns = [
    url(r"^ships/$", ListView.as_view(model=Ship), name="ship_list"),
]
