# Generated by Django 3.1.7 on 2023-11-08 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20231103_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuota',
            name='monto_cuota',
        ),
        migrations.AlterField(
            model_name='cuota',
            name='año',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cuotaanual'),
        ),
        migrations.AlterField(
            model_name='cuotaanual',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
