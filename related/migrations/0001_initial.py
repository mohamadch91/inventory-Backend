# Generated by Django 4.0.6 on 2022-08-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='relatedFacility',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('required', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]