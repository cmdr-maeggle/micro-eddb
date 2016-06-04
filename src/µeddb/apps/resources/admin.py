# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Resource

@admin.register(Resource)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("type", "name", "grade", "description")
    list_display_links = ("name",)