# Generated by Django 4.0.6 on 2022-08-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='abr',
            field=models.FileField(null=True, upload_to='help'),
        ),
    ]