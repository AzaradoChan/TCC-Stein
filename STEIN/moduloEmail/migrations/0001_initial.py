# Generated by Django 4.1 on 2022-11-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAnonimo',
            fields=[
                ('codigoUnico', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
