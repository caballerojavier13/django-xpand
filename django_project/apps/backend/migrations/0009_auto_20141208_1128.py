# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20141208_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_pedido',
            old_name='pedido_venta',
            new_name='pedido',
        ),
    ]
