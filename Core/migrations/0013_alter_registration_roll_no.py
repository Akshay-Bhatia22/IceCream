# Generated by Django 3.2.4 on 2023-04-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_alter_registration_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='roll_no',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
