# Generated by Django 3.0.2 on 2020-02-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0016_auto_20200201_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ost_count',
            field=models.IntegerField(default=0, verbose_name='Остаток копий'),
        ),
    ]
