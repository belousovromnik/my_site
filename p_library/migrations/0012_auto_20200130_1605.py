# Generated by Django 3.0.2 on 2020-01-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
        ('p_library', '0011_auto_20191210_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookreader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100, null=True, unique=True, verbose_name='Комментарий')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.Reader')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(through='p_library.Bookreader', to='reader.Reader'),
        ),
    ]
