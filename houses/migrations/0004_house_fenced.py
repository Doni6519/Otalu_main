# Generated by Django 4.0.2 on 2022-02-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='fenced',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
    ]
