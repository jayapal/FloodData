# Generated by Django 3.1.4 on 2021-01-27 13:00

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geousda',
            name='poly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4269),
        ),
    ]
