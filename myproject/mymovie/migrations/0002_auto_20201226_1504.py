# Generated by Django 3.1 on 2020-12-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='show_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]