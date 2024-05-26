# Generated by Django 5.0.6 on 2024-05-24 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('title', models.TextField()),
                ('description', models.TextField(null=True)),
                ('prerequisites', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20)),
                ('prerequisite_code', models.CharField(max_length=20)),
                ('group_num', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='scraperapp.course')),
                ('prerequisite_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prerequisite_id', to='scraperapp.course')),
                ('subject_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='subject_id', to='scraperapp.subject')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='scraperapp.subject'),
        ),
    ]
