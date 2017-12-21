# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefix',
            name='symbol',
            field=models.CharField(null=True, max_length=5),
        ),
    ]
