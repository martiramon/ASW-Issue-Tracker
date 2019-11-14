# Generated by Django 2.2.7 on 2019-11-07 14:49

import aswissues.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aswissues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='prioritat',
            field=models.CharField(choices=[('Trivial', 'Trivial'), ('Menor', 'Menor'), ('Major', 'Major'), ('Critica', 'Crítica'), ('Bloquejant', 'Bloquejant')], default=aswissues.enums.PrioritatSelector('Trivial'), max_length=200),
        ),
        migrations.AddField(
            model_name='issue',
            name='tipus',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Millora', 'Millora'), ('Proposta', 'Proposta'), ('Tasca', 'Tasca')], default=aswissues.enums.TipusSelector('Millora'), max_length=200),
        ),
    ]
