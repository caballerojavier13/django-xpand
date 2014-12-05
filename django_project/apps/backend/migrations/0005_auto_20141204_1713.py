# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20141204_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico_precio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('producto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Producto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='producto',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Producto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='venta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Venta', null=True),
            preserve_default=True,
        ),
    ]
