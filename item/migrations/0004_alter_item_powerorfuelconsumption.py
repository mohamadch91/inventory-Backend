# Generated by Django 4.0.6 on 2022-09-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_created_at_item_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='PowerOrFuelConsumption',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]