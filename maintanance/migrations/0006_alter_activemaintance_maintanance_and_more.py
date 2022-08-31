# Generated by Django 4.0.6 on 2022-08-31 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_created_at_item_updated_at'),
        ('maintanance', '0005_todomaintance_donemaintance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activemaintance',
            name='maintanance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintanance.maintanance'),
        ),
        migrations.AlterField(
            model_name='activemaintance',
            name='maintanncegp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintanance.maintancegp'),
        ),
        migrations.AlterField(
            model_name='donemaintance',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='item.item'),
        ),
        migrations.AlterField(
            model_name='donemaintance',
            name='maintanance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintanance.maintanance'),
        ),
        migrations.AlterField(
            model_name='donemaintance',
            name='maintanncegp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintanance.maintancegp'),
        ),
        migrations.AlterField(
            model_name='todomaintance',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='item.item'),
        ),
        migrations.AlterField(
            model_name='todomaintance',
            name='maintanance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintanance.maintanance'),
        ),
        migrations.AlterField(
            model_name='todomaintance',
            name='maintanncegp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maintanance.maintancegp'),
        ),
    ]