# Generated by Django 4.0 on 2021-12-23 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Atracao',
            new_name='Atracoes',
        ),
    ]
