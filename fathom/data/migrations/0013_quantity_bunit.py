# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20171221_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='bunit',
            field=models.ForeignKey(to='data.Unit', related_name='quantity_unit', null=True),
        ),
    ]
