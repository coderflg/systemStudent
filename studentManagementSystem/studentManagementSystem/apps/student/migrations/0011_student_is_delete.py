# Generated by Django 3.2.8 on 2021-11-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_student_idcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
