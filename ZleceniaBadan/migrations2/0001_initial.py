# Generated by Django 3.0.4 on 2020-03-15 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DodatkoweBadania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edycja', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Dodatkowe Badanie',
                'verbose_name_plural': 'Dodatkowe Badania',
            },
        ),
        migrations.CreateModel(
            name='Imię',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=128)),
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
                ('nazwisko', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Nazwisko',
                'verbose_name_plural': 'Nazwiska',
            },
        ),
        migrations.CreateModel(
            name='Placowka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=128)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Placowka',
                'verbose_name_plural': 'Placowki',
            },
        ),
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizacja', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Termin',
                'verbose_name_plural': 'Terminy',
            },
        ),
        migrations.CreateModel(
            name='WynikiBadań',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wynik', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Wynik',
                'verbose_name_plural': 'Wyniki',
            },
        ),
        migrations.CreateModel(
            name='ZleceniaBadan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badanie', models.CharField(max_length=128)),
                ('opis', models.TextField(blank=True)),
                ('wynik', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('data_wystawienia', models.DateField(blank=True, null=True)),
                ('dodatkowe_badania', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.DodatkoweBadania')),
                ('imię', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Imię')),
                ('nazwisko', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Nazwisko')),
                ('placówka', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Placowka')),
                ('termin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Termin')),
            ],
            options={
                'verbose_name': 'Zlecenie Badania',
                'verbose_name_plural': 'Zlecenie Badań',
            },
        ),
    ]