# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_quantity_bunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
    ]
