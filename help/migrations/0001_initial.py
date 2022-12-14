# Generated by Django 4.0.6 on 2022-09-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(blank=True, choices=[('dashboard', 'Dashboard'), ('facilities', 'Facilities'), ('hr', 'Hr'), ('user', 'User'), ('message', 'Message'), ('reports', 'Reports'), ('settings', 'Settings'), ('about-iga', 'About Iga')], max_length=20, null=True)),
                ('lang', models.CharField(blank=True, choices=[('en', 'En'), ('fr', 'Fr'), ('ar', 'Ar'), ('fa', 'Fa'), ('es', 'Es'), ('ru', 'Ru')], max_length=20, null=True)),
                ('abr', models.FileField(blank=True, null=True, upload_to='help')),
            ],
        ),
    ]
