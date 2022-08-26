# Generated by Django 4.0.6 on 2022-08-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Cedula', models.FloatField()),
                ('cargo', models.CharField(max_length=50)),
                ('Fecha_inicio', models.FloatField()),
                ('Salario', models.FloatField()),
                ('Tipo_de_contrato', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]