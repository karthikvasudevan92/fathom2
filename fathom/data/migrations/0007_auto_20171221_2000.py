# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20171221_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='terms',
            field=models.ManyToManyField(blank=True, to='data.Term'),
        ),
    ]
