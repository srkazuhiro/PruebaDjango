# Generated by Django 3.1.1 on 2020-11-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=15, verbose_name='usuario')),
                ('contrasena', models.CharField(max_length=15, verbose_name='contraseña')),
                ('nom_cliente', models.CharField(max_length=15, verbose_name='nombre cliente')),
                ('correo', models.CharField(max_length=30, null=True, verbose_name='correo')),
            ],
        ),
        migrations.CreateModel(
            name='cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cuenta', models.IntegerField(verbose_name='tipo cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='cuadro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cuadro', models.CharField(max_length=10, verbose_name='id cuadro')),
                ('cuadro', models.CharField(max_length=20, verbose_name='cuadro')),
                ('precio', models.CharField(max_length=15, verbose_name='precio')),
            ],
        ),
    ]
