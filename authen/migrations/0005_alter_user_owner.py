# Generated by Django 4.0.6 on 2022-09-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_user_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='owner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
