# Generated by Django 4.0.6 on 2022-08-19 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PQS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pqs3',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pqs3',
            name='tempzone',
        ),
        migrations.RemoveField(
            model_name='pqs3',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='pqs3',
            name='waterpackstoragecapacity',
        ),
        migrations.RemoveField(
            model_name='pqs3',
            name='weight',
        ),
    ]
