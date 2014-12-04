# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20141203_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='email',
            field=models.EmailField(default='empresa@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefono',
            field=localflavor.us.models.PhoneNumberField(default=2635863489, max_length=20),
            preserve_default=False,
        ),
    ]
