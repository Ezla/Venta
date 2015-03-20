# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=48)),
                ('descripcion', models.CharField(max_length=100)),
                ('p_unitario', models.DecimalField(max_digits=8, decimal_places=2)),
                ('p_mayoreo', models.DecimalField(max_digits=8, decimal_places=2)),
                ('Inventario', models.BooleanField(default=False)),
                ('Cantidad', models.IntegerField(null=True, blank=True)),
                ('minimo', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
