# Generated by Django 3.1.7 on 2023-10-23 22:06

import autoslug.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_front_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='noticias/')),
                ('fecha', models.DateField()),
                ('resumen', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titulo')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
                ('is_aprobado', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('is_pendiente', models.BooleanField(default=True, verbose_name='Pendiente')),
                ('img1', models.ImageField(blank=True, upload_to='noticias/')),
                ('img2', models.ImageField(blank=True, upload_to='noticias/')),
                ('img3', models.ImageField(blank=True, upload_to='noticias/')),
                ('img4', models.ImageField(blank=True, upload_to='noticias/')),
                ('img5', models.ImageField(blank=True, upload_to='noticias/')),
                ('comentario', models.TextField(default='Sin comentario')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['fecha'],
            },
        ),
    ]
