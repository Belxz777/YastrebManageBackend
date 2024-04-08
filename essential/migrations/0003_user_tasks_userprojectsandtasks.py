# Generated by Django 5.0.2 on 2024-04-08 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essential', '0002_alter_project_todo_alter_task_stageat'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tasks',
            field=models.ManyToManyField(to='essential.task'),
        ),
        migrations.CreateModel(
            name='UserProjectsAndTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essential.user')),
            ],
        ),
    ]
