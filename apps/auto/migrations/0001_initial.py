# Generated by Django 4.1.4 on 2023-01-13 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('idpbv', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=15)),
                ('cc', models.IntegerField()),
                ('especificaciones', models.TextField()),
            ],
        ),
    ]
