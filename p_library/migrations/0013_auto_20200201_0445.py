# Generated by Django 3.0.2 on 2020-02-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
        ('p_library', '0012_auto_20200130_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(null=True, through='p_library.Bookreader', to='reader.Reader'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_release',
            field=models.SmallIntegerField(null=True, verbose_name='Год издания'),
        ),
    ]
