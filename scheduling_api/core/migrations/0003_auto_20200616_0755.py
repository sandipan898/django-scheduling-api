# Generated by Django 3.0.7 on 2020-06-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200615_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulecall',
            name='site_url',
            field=models.CharField(max_length=300),
        ),
    ]
