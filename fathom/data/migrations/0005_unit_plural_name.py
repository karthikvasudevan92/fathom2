# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_unit_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='plural_name',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
