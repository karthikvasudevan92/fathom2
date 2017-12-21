# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quantity',
            options={'verbose_name_plural': 'quantities'},
        ),
        migrations.AddField(
            model_name='unit',
            name='quantity',
            field=models.ForeignKey(to='data.Quantity', null=True),
        ),
    ]
