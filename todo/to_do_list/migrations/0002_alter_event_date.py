# Generated by Django 4.2.4 on 2023-08-25 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default='2000-11-29T11:11', unique=True, verbose_name=''),
        ),
    ]