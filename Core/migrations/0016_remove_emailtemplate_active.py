# Generated by Django 3.2.4 on 2022-11-11 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_auto_20221111_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtemplate',
            name='active',
        ),
    ]
