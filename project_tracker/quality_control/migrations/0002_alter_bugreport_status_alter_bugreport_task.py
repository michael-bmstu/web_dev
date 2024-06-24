# Generated by Django 5.0.4 on 2024-04-28 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='status',
            field=models.CharField(choices=[('New', 'Новый'), ('In_progress', 'В работе'), ('Completed', 'Завершен')], default='New', max_length=50),
        ),
        migrations.AlterField(
            model_name='bugreport',
            name='task',
            field=models.ForeignKey(blank=True, limit_choices_to={'project': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugs', to='tasks.project')}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bugs', to='tasks.task'),
        ),
    ]
