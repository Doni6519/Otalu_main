# Generated by Django 4.0.2 on 2022-02-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
