# Generated by Django 3.0.2 on 2020-02-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0015_auto_20200201_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreader',
            name='datain',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookreader',
            name='dataout',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]