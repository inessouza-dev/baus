# Generated by Django 4.2.1 on 2023-05-17 00:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_baus', '0006_remove_voluntarios_data_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntarios',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
