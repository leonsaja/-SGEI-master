# Generated by Django 3.2.6 on 2021-08-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name='Data nascimento'),
        ),
    ]
