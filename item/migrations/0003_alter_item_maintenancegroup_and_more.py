# Generated by Django 4.0.6 on 2022-12-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_maintenancegroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='MaintenanceGroup',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='OtherFieldsItem1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]