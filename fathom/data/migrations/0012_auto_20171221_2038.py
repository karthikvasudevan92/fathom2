# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_prefix_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefix',
            name='base',
            field=models.IntegerField(default=10),
        ),
    ]
