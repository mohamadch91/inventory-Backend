# Generated by Django 4.0.6 on 2022-08-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('related', '0005_alter_relatedfacility_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedfacility',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
