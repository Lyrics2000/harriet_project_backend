# Generated by Django 3.2.8 on 2021-11-29 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20211129_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowerassets',
            old_name='bank_statement',
            new_name='statement_statement',
        ),
        migrations.RemoveField(
            model_name='borrowerassets',
            name='mpesa_statement',
        ),
    ]
