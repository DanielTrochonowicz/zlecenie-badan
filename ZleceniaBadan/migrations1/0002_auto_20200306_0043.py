
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placowka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Placowka',
                'verbose_name_plural': 'Placowki',
            },
        ),
        migrations.AlterModelOptions(
            name='zleceniabadan',
            options={'verbose_name': 'Zlecenie Badania', 'verbose_name_plural': 'Zlecenie Badań'},
        ),
    ]
