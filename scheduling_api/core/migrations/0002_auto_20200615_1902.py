# Generated by Django 3.0.6 on 2020-06-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.URLField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='PostArticle',
        ),
    ]
