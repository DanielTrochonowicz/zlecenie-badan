# Generated by Django 3.0.4 on 2020-03-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0008_auto_20200313_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='zleceniabadan',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
