# Generated by Django 4.2.7 on 2023-11-17 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="amount",
            new_name="balance",
        ),
    ]
