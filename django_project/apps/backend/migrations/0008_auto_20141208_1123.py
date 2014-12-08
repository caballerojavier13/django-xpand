# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20141205_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_pedido',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='pedido_venta',
            field=models.ForeignKey(null=True, to='backend.Pedido', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='precio',
            field=models.ForeignKey(null=True, to='backend.Historico_precio', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='producto',
            field=models.ForeignKey(null=True, to='backend.Producto', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='descuento',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='descuento',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
