# Generated by Django 3.0.2 on 2020-02-01 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
        ('p_library', '0013_auto_20200201_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(through='p_library.Bookreader', to='reader.Reader'),
        ),
        migrations.AlterField(
            model_name='bookreader',
            name='reader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reader.Reader'),
        ),
    ]
