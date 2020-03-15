# Generated by Django 3.0.4 on 2020-03-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0015_auto_20200313_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='WynikiBadań',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wynik', models.CharField(max_length=328)),
            ],
            options={
                'verbose_name': 'Wynik',
                'verbose_name_plural': 'Wyniki',
            },
        ),
        migrations.AddField(
            model_name='zleceniabadan',
            name='wynik',
            field=models.TextField(blank=True),
        ),
    ]
