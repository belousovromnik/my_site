# Generated by Django 2.2.4 on 2019-12-10 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20191210_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubhouse',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='p_library.PubHouse', verbose_name='Издательство'),
        ),
    ]