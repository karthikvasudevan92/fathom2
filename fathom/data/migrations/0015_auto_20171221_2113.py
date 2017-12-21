# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20171221_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
    ]
