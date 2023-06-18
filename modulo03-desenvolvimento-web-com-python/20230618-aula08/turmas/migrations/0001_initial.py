# Generated by Django 4.2.2 on 2023-06-18 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('qtd_minimo_alunos', models.IntegerField(default=0)),
                ('qtd_maxima_alunos', models.IntegerField(default=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos')),
                ('instrutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_turmas',
            },
        ),
    ]
