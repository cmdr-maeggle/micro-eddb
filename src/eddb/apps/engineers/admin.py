# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Engineer, Blueprint, BlueprintRequirement


@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "blueprints",
    )


@admin.register(Blueprint)
class BlueprintAdmin(admin.ModelAdmin):
    ordering = ["name", "grade"]
    list_display = ("module_type", "name", "grade")
    list_display_links = ("name",)

    class BlueprintRequirementInline(admin.TabularInline):
        model = BlueprintRequirement
        max_num = 5

    class EngineerInline(admin.TabularInline):
        model = Engineer.blueprints.through

    inlines = [
        BlueprintRequirementInline,
        EngineerInline
    ]


@admin.register(BlueprintRequirement)
class BlueprintRequirementAdmin(admin.ModelAdmin):
    ordering = ["blueprint__name", "blueprint__grade", "resource__name"]
    list_display = ("blueprint_name", "resource", "amount")
    list_display_links = ("resource",)
    list_select_related = ("blueprint", "resource", "blueprint__module_type")
    list_editable = ("amount",)

    def blueprint_name(self, obj: BlueprintRequirement):
        return "{0}: {1}, Grade {2}".format(obj.blueprint.module_type.name, obj.blueprint.name, obj.blueprint.grade)
    blueprint_name.short_description = "Blueprint"
