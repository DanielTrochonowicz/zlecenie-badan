# Generated by Django 3.0.4 on 2020-03-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZleceniaBadan', '0027_auto_20200315_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(blank=True, default=0, max_length=120),
        ),
    ]
