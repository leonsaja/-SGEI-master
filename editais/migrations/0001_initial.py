# Generated by Django 3.2.6 on 2021-09-08 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('peso', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Alternativas',
                'verbose_name_plural': 'Alternativa',
            },
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('ab', 'Aberto'), ('em', 'Em Analise'), ('fn', 'Finalizado')], default='ab', max_length=2)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='edital/banner')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='edital/pdf')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Editais',
                'verbose_name_plural': 'Edital',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('df', 'Deferido'), ('in', 'Indeferido'), ('an', 'Em Analise')], default='an', max_length=2)),
                ('nivel_vul', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.edital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inscrições',
                'verbose_name_plural': 'Inscrição',
                'ordering': ['-nivel_vul'],
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('is_aberta', models.BooleanField(default=False, null=True)),
                ('has_arquivo', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.edital')),
            ],
            options={
                'verbose_name': 'Perguntas',
                'verbose_name_plural': 'Pergunta',
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='inscricoes')),
                ('resposta_aberta', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alternativa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editais.alternativa')),
                ('inscricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.inscricao')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.pergunta')),
            ],
            options={
                'verbose_name': 'Respostas',
                'verbose_name_plural': 'Resposta',
            },
        ),
        migrations.AddField(
            model_name='alternativa',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editais.pergunta'),
        ),
    ]
