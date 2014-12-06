# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_detalle_venta_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
