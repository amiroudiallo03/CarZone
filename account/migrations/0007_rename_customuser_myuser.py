# Generated by Django 4.0.1 on 2022-01-12 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carzoneapp', '0004_initial'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('account', '0006_rename_account_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='MyUser',
        ),
    ]
