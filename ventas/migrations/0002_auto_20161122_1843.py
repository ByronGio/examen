# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Existencia',
            new_name='existencia',
        ),
    ]
