# Generated by Django 2.1.4 on 2019-03-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0016_auto_20190321_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
