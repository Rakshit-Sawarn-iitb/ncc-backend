# Generated by Django 5.0.6 on 2024-05-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CouncilCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=400)),
            ],
        ),
    ]
