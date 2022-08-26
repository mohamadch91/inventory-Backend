# Generated by Django 4.0.6 on 2022-08-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintanance', '0002_maintanance_requires'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintanance',
            name='enable',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.CreateModel(
            name='activeMaintance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('enable', models.BooleanField(blank=True, default=True, null=True)),
                ('maintanance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintanance.maintanance')),
            ],
        ),
    ]
