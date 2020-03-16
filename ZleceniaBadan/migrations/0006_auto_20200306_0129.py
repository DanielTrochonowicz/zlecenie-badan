
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0005_auto_20200306_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imię',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Imię',
                'verbose_name_plural': 'Imiona',
            },
        ),
        migrations.CreateModel(
            name='Nazwisko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwisko', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Nazwisko',
                'verbose_name_plural': 'Nazwiska',
            },
        ),
        migrations.AddField(
            model_name='zleceniabadan',
            name='imię',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Imię'),
        ),
        migrations.AddField(
            model_name='zleceniabadan',
            name='nazwisko',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Nazwisko'),
        ),
    ]
