# Generated by Django 3.1.7 on 2023-10-29 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listado',
            options={'ordering': ['tipo', 'order'], 'verbose_name': 'Listado', 'verbose_name_plural': 'Listados'},
        ),
    ]