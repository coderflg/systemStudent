# Generated by Django 3.2.8 on 2021-11-26 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_classroom_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='student_id',
        ),
    ]