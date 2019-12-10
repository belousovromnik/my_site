# Generated by Django 2.2.4 on 2019-12-10 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20191210_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pubhouse',
            name='books',
        ),
        migrations.AddField(
            model_name='pubhouse',
            name='books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='p_library.Book', verbose_name='Книга'),
            preserve_default=False,
        ),
    ]
