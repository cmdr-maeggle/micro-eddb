# -*- coding: utf-8 -*-

from django.db import models


PAD_SIZE_CHOICES = (
    ("S", "small"),
    ("M", "medium"),
    ("L", "large"),
)

class Manufacturer(models.Model):
    """
    A ship manufacturer in the Elite universe.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ship(models.Model):
    """
    A ship, that you can fly in the game (or not)
    """

    class Meta(object):
        unique_together = (
            ("manufacturer", "name"),
        )

    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=100)
    pad_size = models.CharField(max_length=1, default="", choices=PAD_SIZE_CHOICES)

    def __str__(self):
        return "{0.manufacturer} {0.name}".format(self)


class ModuleType(models.Model):
    class Meta(object):
        ordering = ["name"]

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# class ShipModule(models.Model):
#     ship = models.ForeignKey(Ship)
#     type = models.ForeignKey(ModuleType)
#     size = models.PositiveSmallIntegerField()
