# Generated by Django 3.2.8 on 2021-11-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='header',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='studentManagementSystem/static/headers'),
        ),
    ]