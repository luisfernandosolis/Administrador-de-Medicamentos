# Generated by Django 2.1.4 on 2019-03-22 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0017_auto_20190321_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
