# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_auto_20150301_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='p_mayoreo',
            new_name='pmayoreo',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='p_unitario',
            new_name='punitario',
        ),
    ]
