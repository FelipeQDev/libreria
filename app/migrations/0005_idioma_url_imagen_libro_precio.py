# Generated by Django 4.1.1 on 2022-11-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_autor_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='url_imagen',
            field=models.CharField(default='a', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
