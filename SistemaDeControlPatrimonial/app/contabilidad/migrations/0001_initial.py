# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaContable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('numero_cuenta', models.IntegerField()),
            ],
            options={
                'db_table': 'CuentaContable',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CuentaContableDivisionaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('numero_cuenta', models.IntegerField()),
                ('depreciacion', models.BooleanField()),
                ('cuenta_depreciacion', models.IntegerField()),
            ],
            options={
                'db_table': 'CuentaContableDivisionaria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCuentaContable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('numero_cuenta', models.IntegerField()),
                ('cuenta_contable', models.ForeignKey(to='contabilidad.CuentaContable')),
            ],
            options={
                'db_table': 'SubCuentaContable',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cuentacontabledivisionaria',
            name='sub_cuenta_contable',
            field=models.ForeignKey(to='contabilidad.SubCuentaContable'),
        ),
    ]
