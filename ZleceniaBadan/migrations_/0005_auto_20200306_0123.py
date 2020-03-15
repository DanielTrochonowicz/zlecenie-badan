
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0004_auto_20200306_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='DodatkoweBadania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edycja', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'DodatkoweBadanie',
                'verbose_name_plural': 'DodatkoweBadania',
            },
        ),
        migrations.AddField(
            model_name='zleceniabadan',
            name='dodatkoweBadania',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.DodatkoweBadania'),
        ),
    ]
