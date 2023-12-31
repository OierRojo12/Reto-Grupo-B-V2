# Generated by Django 4.2.7 on 2023-11-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarioBundesliga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(db_column='local')),
                ('visitante', models.CharField(db_column='visitante')),
                ('resultado', models.CharField(db_column='resultado')),
            ],
            options={
                'db_table': 'calendario_bundesliga',
            },
        ),
        migrations.CreateModel(
            name='CalendarioLaLiga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(db_column='local')),
                ('visitante', models.CharField(db_column='visitante')),
                ('resultado', models.CharField(db_column='resultado')),
            ],
            options={
                'db_table': 'calendario_laliga',
            },
        ),
        migrations.CreateModel(
            name='CalendarioLigue1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(db_column='local')),
                ('visitante', models.CharField(db_column='visitante')),
                ('resultado', models.CharField(db_column='resultado')),
            ],
            options={
                'db_table': 'calendario_ligue1',
            },
        ),
        migrations.CreateModel(
            name='CalendarioPremierLeague',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(db_column='local')),
                ('visitante', models.CharField(db_column='visitante')),
                ('resultado', models.CharField(db_column='resultado')),
            ],
            options={
                'db_table': 'calendario_premierleague',
            },
        ),
        migrations.CreateModel(
            name='CalendarioSerieA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(db_column='local')),
                ('visitante', models.CharField(db_column='visitante')),
                ('resultado', models.CharField(db_column='resultado')),
            ],
            options={
                'db_table': 'calendario_seriea',
            },
        ),
    ]
