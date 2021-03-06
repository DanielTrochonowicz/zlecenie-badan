# Generated by Django 3.0.4 on 2020-03-13 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0016_auto_20200313_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='WynikPN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wynikPN', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'wynikPN',
                'verbose_name_plural': 'wynikiPN',
            },
        ),
        migrations.AlterField(
            model_name='zleceniabadan',
            name='wynik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.WynikPN'),
        ),
    ]
