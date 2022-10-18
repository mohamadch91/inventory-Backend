# Generated by Django 4.0.6 on 2022-10-18 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
        ('message', '0002_message_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='readedMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.message')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facilities.facility')),
            ],
        ),
    ]
