# Generated by Django 4.0.4 on 2022-05-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armazem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='nida',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
