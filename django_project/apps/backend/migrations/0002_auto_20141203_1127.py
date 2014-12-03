# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='backend.Domicilio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=localflavor.us.models.PhoneNumberField(max_length=20),
            preserve_default=True,
        ),
    ]
