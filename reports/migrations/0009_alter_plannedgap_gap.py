# Generated by Django 4.0.6 on 2022-09-02 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_plannedgap_asiign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plannedgap',
            name='gap',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='saved_gap', to='reports.gapsave'),
        ),
    ]