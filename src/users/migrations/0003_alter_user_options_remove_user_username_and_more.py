# Generated by Django 4.2.6 on 2023-11-23 18:37
# mypy: ignore-errors
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_is_active_alter_user_role"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
