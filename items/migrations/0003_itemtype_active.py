# Generated by Django 4.0.6 on 2022-08-12 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_itemtype_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtype',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
