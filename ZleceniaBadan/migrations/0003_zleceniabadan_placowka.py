
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0002_auto_20200306_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='zleceniabadan',
            name='placowka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ZleceniaBadan.Placowka'),
        ),
    ]
