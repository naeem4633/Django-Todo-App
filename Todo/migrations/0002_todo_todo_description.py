# Generated by Django 4.1.7 on 2023-03-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_description',
            field=models.TextField(null=True),
        ),
    ]
