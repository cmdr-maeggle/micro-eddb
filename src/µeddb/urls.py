# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from django.views.generic import TemplateView

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="index.html")),
    url(r"^ships/", include("µeddb.apps.ships.urls")),
    url(r"^engineers/", include("µeddb.apps.engineers.urls")),
    url(r"^resources/", include("µeddb.apps.resources.urls")),
]
