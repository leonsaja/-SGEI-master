# Generated by Django 3.2.6 on 2021-08-14 23:03

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210814_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='CPF'),
        ),
    ]