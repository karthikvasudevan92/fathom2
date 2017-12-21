# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20171221_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
