# Generated by Django 4.2.4 on 2023-08-24 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.TimeField()),
                ('color', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(default='blue', max_length=200),
        ),
        migrations.AddField(
            model_name='routine',
            name='repeat',
            field=models.JSONField(default={'Thursday': False}),
        ),
    ]