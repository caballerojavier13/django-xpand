# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20141204_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_venta',
            name='precio',
            field=models.ForeignKey(to='backend.Historico_precio', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
            preserve_default=True,
        ),
    ]
