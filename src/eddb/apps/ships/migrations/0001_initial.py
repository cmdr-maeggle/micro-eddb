# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pad_size', models.CharField(choices=[('S', 'small'), ('M', 'medium'), ('L', 'large')], default='', max_length=1)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.Manufacturer')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ship',
            unique_together=[('manufacturer', 'name')],
        ),
    ]
