# Generated by Django 3.0.4 on 2020-03-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0002_auto_20200315_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(3, 'BARDZO_ZLY'), (2, 'SLABY'), (0, 'Nieznany'), (3, 'NIE_WYLECZALNY'), (1, 'DOBRY')], default=0),
        ),
    ]