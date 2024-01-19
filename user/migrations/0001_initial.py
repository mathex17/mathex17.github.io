# Generated by Django 4.0.6 on 2022-07-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30, verbose_name='Nombres')),
                ('LastName', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('Phone', models.CharField(max_length=10, verbose_name='Telefono')),
                ('Direction', models.TextField(verbose_name='Dirección')),
                ('Email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('Password', models.CharField(max_length=32, verbose_name='Contraseña')),
            ],
        ),
    ]