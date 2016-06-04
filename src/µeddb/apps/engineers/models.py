# -*- coding: utf-8 -*-

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Engineer(models.Model):
    """
    Engineers with backstories written by Michael effin Brookes...
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")

    blueprints = models.ManyToManyField("Blueprint")


class Blueprint(models.Model):
    """
    Blueprints are used to craft upgrades for a ship's module.
    """

    name = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    module_type = models.ForeignKey("ships.ModuleType", null=True)

    def __str__(self):
        return "{bp.module_type}: {bp.name}, grade {bp.grade}".format(bp=self)


class BlueprintRequirement(models.Model):
    """
    A modification requirement is just that - a material, some data or a commodity
    used in crafting a certain modification. It is agnostic of
    """

    blueprint = models.ForeignKey("Blueprint", related_name="requirements")
    resource = models.ForeignKey("resources.Resource", related_name="required_for")
    amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "{r.blueprint.name}: {r.amount}x {r.resource}".format(r=self)
