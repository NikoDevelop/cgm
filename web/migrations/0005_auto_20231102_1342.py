# Generated by Django 3.1.7 on 2023-11-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_cuota_cuotaanual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuotaanual',
            name='fecha_creacion',
            field=models.DateField(verbose_name='Fecha de creacion'),
        ),
    ]
