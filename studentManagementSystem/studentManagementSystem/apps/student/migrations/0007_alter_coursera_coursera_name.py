# Generated by Django 3.2.8 on 2021-11-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20211127_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursera',
            name='coursera_name',
            field=models.CharField(default=None, max_length=18),
        ),
    ]