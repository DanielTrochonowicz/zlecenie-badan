# Generated by Django 3.0.4 on 2020-03-15 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.IntegerField(default=0)),
                ('rodzaj', models.IntegerField(choices=[(1, 'DOBRY'), (0, 'Nieznany'), (2, 'SLABY'), (3, 'BARDZO_ZLY'), (3, 'NIE_WYLECZALNY')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='zleceniabadan',
            name='id',
        ),
        migrations.AddField(
            model_name='zleceniabadan',
            name='info',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ZleceniaBadan.ExtraInfo'),
            preserve_default=False,
        ),
    ]
