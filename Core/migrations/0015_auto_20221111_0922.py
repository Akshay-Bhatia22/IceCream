# Generated by Django 3.2.4 on 2022-11-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_emailtemplate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailtemplate',
            old_name='subject',
            new_name='subject_alternate',
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='subject_primary',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
