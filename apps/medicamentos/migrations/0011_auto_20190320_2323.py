# Generated by Django 2.1.4 on 2019-03-21 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0010_auto_20190320_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informedeconsumo',
            name='saldoDisponible',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='informedeconsumo',
            name='totalsalida',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='informedeconsumo',
            name='valorE',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='informedeconsumo',
            name='valorS',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='informedeconsumo',
            name='ventaexterna',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='informedeconsumo',
            name='ventasis',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
