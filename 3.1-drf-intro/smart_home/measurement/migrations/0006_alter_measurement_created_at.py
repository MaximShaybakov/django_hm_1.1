# Generated by Django 4.0.6 on 2022-09-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created_at'),
        ),
    ]