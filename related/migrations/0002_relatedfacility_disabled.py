# Generated by Django 4.0.6 on 2022-08-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('related', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedfacility',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]