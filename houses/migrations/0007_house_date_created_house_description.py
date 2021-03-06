# Generated by Django 4.0.2 on 2022-02-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_house_water_availability_alter_house_water'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
