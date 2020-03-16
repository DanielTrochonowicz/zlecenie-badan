
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZleceniaBadan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badanie', models.CharField(max_length=128)),
                ('opis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=99999)),
            ],
        ),
    ]
