# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Manufacturer, Ship, ModuleType



admin.site.register(Manufacturer)
admin.site.register(ModuleType)

@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "name", "pad_size")
    list_display_links = ("name",)

    def manufacturer(self, obj):
        return obj.manufacturer.name
    manufacturer.admin_order_field = "manufacturer__name"
