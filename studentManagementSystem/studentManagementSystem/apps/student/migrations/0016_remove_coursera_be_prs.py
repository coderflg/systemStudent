# Generated by Django 3.2.8 on 2021-11-29 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_rename_be_pr_coursera_be_prs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursera',
            name='be_prs',
        ),
    ]
