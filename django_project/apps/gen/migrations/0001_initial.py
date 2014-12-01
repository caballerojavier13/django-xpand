# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Almacen_producto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.IntegerField()),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='gen.Almacen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.DecimalField(max_digits=12, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('piso', models.IntegerField()),
                ('departamento', models.IntegerField()),
                ('localidad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('lema', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('domicilio', models.ForeignKey(to='gen.Domicilio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('categoria', models.ForeignKey(to='gen.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='domicilio',
            field=models.ForeignKey(to='gen.Domicilio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='almacen_producto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='gen.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='almacen',
            name='domicilio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='gen.Domicilio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='almacen',
            name='empresa',
            field=models.ForeignKey(to='gen.Empresa'),
            preserve_default=True,
        ),
    ]
