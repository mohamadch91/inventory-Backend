# Generated by Django 4.0.6 on 2022-08-03 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facilityid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facilities.facility'),
        ),
    ]
