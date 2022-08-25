# Generated by Django 4.0.6 on 2022-08-22 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_manufacturer'),
        ('related', '0008_itemvalidation_facilityvalidation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilityparam',
            name='fieldid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facfieldid', to='related.relatedfacility'),
        ),
        migrations.AlterField(
            model_name='facilityparamdescription',
            name='paramid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facparamid', to='related.facilityparam'),
        ),
        migrations.AlterField(
            model_name='facilityvalidation',
            name='fieldid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facvalfieldid', to='related.relatedfacility'),
        ),
        migrations.AlterField(
            model_name='itemparam',
            name='fieldid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paramfieldid', to='related.field'),
        ),
        migrations.AlterField(
            model_name='itemparamdescription',
            name='paramid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemparamid', to='related.itemparam'),
        ),
        migrations.AlterField(
            model_name='itemvalidation',
            name='fieldid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemvalfieldid', to='related.field'),
        ),
        migrations.AlterField(
            model_name='relateditemtype',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_field', to='related.field'),
        ),
        migrations.AlterField(
            model_name='relateditemtype',
            name='itemtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_itemtype', to='items.itemtype'),
        ),
    ]