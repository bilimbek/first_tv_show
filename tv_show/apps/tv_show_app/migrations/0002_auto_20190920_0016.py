# Generated by Django 2.2.5 on 2019-09-20 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='Network',
            new_name='network',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='Release_Date',
            new_name='release',
        ),
    ]
