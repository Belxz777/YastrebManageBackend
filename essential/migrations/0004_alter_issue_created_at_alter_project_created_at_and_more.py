# Generated by Django 5.0.2 on 2024-04-24 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential', '0003_rename_issues_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='created_at',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
