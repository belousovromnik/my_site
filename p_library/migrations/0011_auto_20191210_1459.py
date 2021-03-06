# Generated by Django 2.2.4 on 2019-12-10 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0010_auto_20191210_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubhouse',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='book', to='p_library.PubHouse', verbose_name='Издательство'),
            preserve_default=False,
        ),
    ]
