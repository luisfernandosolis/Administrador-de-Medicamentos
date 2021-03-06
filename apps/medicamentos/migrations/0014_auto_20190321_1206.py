# Generated by Django 2.1.4 on 2019-03-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0013_auto_20190320_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='ingreso',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.RemoveField(
            model_name='medication',
            name='typePresentation',
        ),
        migrations.AddField(
            model_name='medication',
            name='typePresentation',
            field=models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to='medicamentos.typeOfPresentation'),
        ),
        migrations.RemoveField(
            model_name='ventasmes',
            name='tipo',
        ),
        migrations.AddField(
            model_name='ventasmes',
            name='tipo',
            field=models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to='medicamentos.TipoVenta'),
        ),
    ]
