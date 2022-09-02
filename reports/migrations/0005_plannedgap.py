# Generated by Django 4.0.6 on 2022-09-02 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0006_alter_facility_working_from_and_more'),
        ('reports', '0004_gapsave_calculate_for'),
    ]

    operations = [
        migrations.CreateModel(
            name='plannedGap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pqs_type', models.IntegerField()),
                ('pqs_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='saved_gap', to='facilities.facility')),
            ],
        ),
    ]
