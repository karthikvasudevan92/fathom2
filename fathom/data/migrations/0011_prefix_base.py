# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_prefix_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefix',
            name='base',
            field=models.IntegerField(max_length=10, default=10),
        ),
    ]
