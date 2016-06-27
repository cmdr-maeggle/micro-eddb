# -*- coding: utf-8 -*-

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q, F, Max

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

    def module_upgrades(self):
        module_upgrades = (self.blueprints
                           .annotate(module_name=F("module_type__name"))
                           .values("module_name")
                           .annotate(grade_max=Max("grade"))
                           .order_by("grade_max", "module_name"))
        return module_upgrades


class Blueprint(models.Model):
    """
    Blueprints are used to craft upgrades for a ship's module.
    """

    name = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField(choices=BLUEPRINT_GRADE_CHOICES)
    module_type = models.ForeignKey("ships.ModuleType", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{bp.name}, grade {bp.grade}".format(bp=self)


class BlueprintRequirement(models.Model):
    """
    A modification requirement is just that - a material, some data or a commodity
    used in crafting a certain modification. It is agnostic of
    """

    blueprint = models.ForeignKey("Blueprint", related_name="requirements", on_delete=models.CASCADE)
    resource = models.ForeignKey("resources.Resource", related_name="required_for", on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "{r.blueprint.name}: {r.amount}x {r.resource}".format(r=self)


# Blueprint Effects (Primary) --------------------------------------------------

class BlueprintEffectManager(models.Manager):
    use_for_related_fields = True

    def primary_effects(self):
        qs = self.get_queryset()
        # filter out unnecessary stuff, that went in via EDCA-import
        qs = qs.filter(~Q(range_min=1.0) & ~Q(range_max=1.0))
        # TODO if secondary effects will ever be added to the BlueprintEffect model, add another filter here:
        # TODO qs = qs.filter(effect_type='primary')
        return qs


class BlueprintEffect(models.Model):
    objects = BlueprintEffectManager()

    blueprint = models.ForeignKey(Blueprint, related_name="effects", on_delete=models.CASCADE)
    statistic = models.ForeignKey("ships.ModuleStatistic", related_name="+", on_delete=models.CASCADE)
    gain = models.BooleanField(default=True)
    range_min = models.DecimalField(default=0.0, max_digits=7, decimal_places=5)
    range_max = models.DecimalField(default=0.0, max_digits=7, decimal_places=5)

    def save(self, *args, **kwargs):
        if self.range_min > self.range_max:
            self.range_min, self.range_max = self.range_max, self.range_min
        super().save(*args, **kwargs)

    def __str__(self):
        fmt_data = {'name': self.statistic}
        if self.gain:
            fmt_data.update({
                'g': "G",
                'min': self.range_min,
                'max': self.range_max,
            })
        else:
            fmt_data.update({
                'g': "L",
                'min': self.range_max,
                'max': self.range_min,
            })
        return "{name} ({g}: {min} - {max})".format(**fmt_data)
