# Generated by Django 2.2.4 on 2019-12-10 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20191210_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pubhouse',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='pubhouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='p_library.PubHouse', verbose_name='Издательство'),
            preserve_default=False,
        ),
    ]
