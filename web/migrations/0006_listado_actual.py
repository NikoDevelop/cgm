# Generated by Django 3.1.7 on 2023-10-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20231028_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='listado',
            name='actual',
            field=models.BooleanField(default=False),
        ),
    ]
