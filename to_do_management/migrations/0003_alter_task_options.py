# Generated by Django 5.1.1 on 2024-09-25 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("to_do_management", "0002_alter_task_options_alter_task_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("status", "-created_time")},
        ),
    ]
