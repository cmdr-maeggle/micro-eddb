# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ResourceListView, ResourceDetailView

app_name = "resources"

urlpatterns = [
    url(r"^$", ResourceListView.as_view(), name="index"),
    url(r"^$", ResourceListView.as_view(), name="resource_list"),
    url(r"^resource/(?P<pk>\d+)$", ResourceDetailView.as_view(), name="resource_detail"),
]
