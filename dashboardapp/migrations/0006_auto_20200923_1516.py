# Generated by Django 3.0.6 on 2020-09-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0005_auto_20200923_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doneevents',
            name='upcoming',
            field=models.BooleanField(default=True),
        ),
    ]
