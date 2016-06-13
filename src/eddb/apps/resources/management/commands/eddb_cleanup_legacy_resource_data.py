# -*- coding: utf-8 -*-

"""
Data source: <https://docs.google.com/spreadsheets/d/1wTmKrzLCXRIdHwKHaN-gXHq6YkS_JAnJKsyQp8P-j0Y/edit#gid=93194749>
"""
import re
from django.core.management.base import BaseCommand, CommandError

from eddb.apps.resources.models import Resource


class Command(BaseCommand):
    help = "Cleans existing / legacy resource data, that might be malformatted or inaccurate."

    def handle(self, *args, **options):
        source_pattern = re.compile(r"""^Source: (?P<sources>.*)$""", re.IGNORECASE | re.MULTILINE)

        for resource in Resource.objects.all():
            resource_description = resource.description
            for match in source_pattern.finditer(resource_description):
                wholeline = match.group()
                resource_description = resource_description.replace(wholeline, "")

                sources = match.group("sources")
                for source in sources.split(","):
                    source = source.strip()
                    if not source:
                        continue
                    self.stdout.write(source)
