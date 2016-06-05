# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from django.views.generic import TemplateView

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="index.html")),
    url(r"^ships/", include("eddb.apps.ships.urls")),
    url(r"^engineers/", include("eddb.apps.engineers.urls")),
    url(r"^resources/", include("eddb.apps.resources.urls")),
]
