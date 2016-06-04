# -*- coding: utf-8 -*-

from django.db import models


RESOURCE_TYPE_CHOICES = (
    ('c', "Commodity"),
    ('d', "Data"),
    ('m', "Manufactured"),
    ('r', "Raw Material"),
)

RESOURCE_GRADE_CHOICES = (
    (1, "very common"),
    (2, "common"),
    (3, "normal"),
    (4, "rare"),
    (5, "very rare"),
)


class Resource(models.Model):
    """
    Resources are materials, commodities or data packages, that are scannable or scoopable.
    They are used with the engineers to upgrade ship modules.

    Commodities are also used for trading, but that's won't be covered here.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    type = models.CharField(max_length=1, choices=RESOURCE_TYPE_CHOICES, default='m')
    grade = models.PositiveSmallIntegerField(choices=RESOURCE_GRADE_CHOICES, default=1)

    def __repr__(self):
        return "Resource(name='{0.name}', type='{0.type}')".format(self)

    def __str__(self):
        return self.name or repr(self)
