# Generated by Django 4.2.3 on 2023-07-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0003_rename_qtd_minima_alunos_turma_qtd_minimo_alunos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turma',
            old_name='qtd_minimo_alunos',
            new_name='qtd_minima_alunos',
        ),
    ]