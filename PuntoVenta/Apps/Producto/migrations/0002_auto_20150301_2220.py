# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Cantidad',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Inventario',
            new_name='inventario',
        ),
    ]
