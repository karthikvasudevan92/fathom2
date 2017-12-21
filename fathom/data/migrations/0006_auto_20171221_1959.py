# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_unit_plural_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='terms',
            field=models.ManyToManyField(to='data.Term', null=True),
        ),
    ]
