# Generated by Django 5.0.6 on 2024-05-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilcard',
            name='role',
            field=models.IntegerField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='councilcard',
            name='year',
            field=models.IntegerField(default=False, null=True),
        ),
    ]