# Generated by Django 4.0.6 on 2022-08-21 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('related', '0007_field_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemvalidation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('digits', models.IntegerField(default=0)),
                ('min', models.IntegerField(default=0)),
                ('max', models.IntegerField(default=0)),
                ('float', models.BooleanField(default=False)),
                ('floating', models.IntegerField(default=0)),
                ('fieldid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='related.field')),
            ],
        ),
        migrations.CreateModel(
            name='Facilityvalidation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('digits', models.IntegerField(default=0)),
                ('min', models.IntegerField(default=0)),
                ('max', models.IntegerField(default=0)),
                ('float', models.BooleanField(default=False)),
                ('floating', models.IntegerField(default=0)),
                ('fieldid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='related.relatedfacility')),
            ],
        ),
    ]
