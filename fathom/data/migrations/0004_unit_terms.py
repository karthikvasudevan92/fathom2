# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20171221_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='terms',
            field=models.ManyToManyField(to='data.Term'),
        ),
    ]
