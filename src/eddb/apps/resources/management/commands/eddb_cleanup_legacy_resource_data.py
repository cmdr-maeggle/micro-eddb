# -*- coding: utf-8 -*-

import os.path
import json
import re
from django.core.management.base import BaseCommand

from eddb.apps.resources.models import Resource


class Command(BaseCommand):
    help = "Cleans existing / legacy resource data, that might be malformatted or inaccurate."

    def handle(self, *args, **options):
        legacy_data_path = os.path.join(os.path.dirname(__file__), "legacy_material_data.json")
        with open(legacy_data_path, "r") as legacy_data_file:
            legacy_data = json.loads(legacy_data_file.read())
            for item in legacy_data:
                if not item['model'] == "resources.resource":
                    continue
                resource_name = item['fields']['name']
                resource_grade = item['fields']['grade']
                resource_type = item['fields']['type']
                resource_description = item['fields']['description']

                resource, created = Resource.objects.get_or_create(name=resource_name)
                resource.grade = resource_grade
                resource.type = resource_type
                resource.description = resource_description
                resource.save()

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
