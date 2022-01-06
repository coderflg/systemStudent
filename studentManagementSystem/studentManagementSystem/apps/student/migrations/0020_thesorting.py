# Generated by Django 3.2.8 on 2021-11-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_coursera_is_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheSorting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortingName', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'db_sorting',
                'verbose_name_plural': 'db_sorting',
                'db_table': 'db_sorting',
            },
        ),
    ]