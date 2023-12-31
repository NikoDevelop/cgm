# Generated by Django 3.1.7 on 2023-10-28 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20231028_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='region',
            field=models.CharField(choices=[('I', 'Región de Tarapacá  '), ('II', 'Región de Antofagasta  '), ('III', 'Región de Atacama  '), ('IV', 'Región de Coquimbo  '), ('V', 'Región de Valparaíso    '), ('VI', 'Región del Libertador General Bernardo O’Higgins    '), ('VII', 'Región del Maule    '), ('VIII', 'Región del Bio-bío  '), ('IX', 'Región de La Araucanía  '), ('X', 'Región de Los Lagos '), ('XI', 'Región Aysén del General Carlos Ibáñez del Campo '), ('XII', 'Región de Magallanes y Antártica Chilena   '), ('XIII', 'Región Metropolitana de Santiago    '), ('XIV', 'Región de Los Ríos '), ('XV', 'Región de Arica y Parinacota   '), ('XVI', 'Región de Ñuble ')], default='XIII', max_length=50, verbose_name='Region'),
        ),
    ]
