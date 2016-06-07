# -*- coding: utf-8 -*-

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


ALLEGIENCE_CHOICES = (
    (0, "Indipendent"),
    (1, "Federation"),
    (2, "Empire"),
    (3, "Alliance"),
)

BLUEPRINT_GRADE_CHOICES = (
    (1, "Grade 1"),
    (2, "Grade 2"),
    (3, "Grade 3"),
    (4, "Grade 4"),
    (5, "Grade 5"),
)


class Engineer(models.Model):
    """
    Engineers with backstories written by Michael effin Brookes...
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")
    allegience = models.PositiveSmallIntegerField(default=0, choices=ALLEGIENCE_CHOICES)

    # TODO remove when we can add an actual Station model reference
    location_name = models.CharField(max_length=100, blank=True, default="")

    blueprints = models.ManyToManyField("Blueprint", related_name="engineers")

    def __str__(self):
        return self.name

    @property  # TODO replace with reference to an actual Station model instance (t.b.d.)
    def location(self):
        return self.location_name


class Blueprint(models.Model):
    """
    Blueprints are used to craft upgrades for a ship's module.
    """

    name = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField(choices=BLUEPRINT_GRADE_CHOICES)
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
