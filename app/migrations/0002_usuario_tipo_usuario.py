# Generated by Django 4.1.1 on 2022-11-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
