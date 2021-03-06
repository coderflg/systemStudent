# Generated by Django 3.2.8 on 2021-11-26 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('manager', models.CharField(max_length=66)),
                ('Class_rating', models.CharField(max_length=3)),
                ('class_The_sorting', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '教室',
                'verbose_name_plural': '教室',
                'db_table': 'db_class',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_school', models.DateTimeField(auto_now_add=True, verbose_name='join school date')),
                ('name', models.CharField(default=None, max_length=4, verbose_name='name')),
                ('gender', models.CharField(default=None, max_length=2)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('belong_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belong', to='student.classroom')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'student',
                'db_table': 'db_student',
            },
        ),
    ]
