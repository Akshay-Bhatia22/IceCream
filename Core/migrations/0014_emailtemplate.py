# Generated by Django 3.2.4 on 2022-11-11 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_auto_20221111_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Core.event')),
                ('subject', models.CharField(max_length=200, null=True)),
                ('primary', models.CharField(default='registration-response-email.html', max_length=100)),
                ('alternate', models.CharField(default='', max_length=100)),
                ('active', models.CharField(choices=[('primary', 'primary'), ('alternate', 'alterante')], max_length=100)),
                ('primary_limit', models.IntegerField()),
            ],
        ),
    ]
