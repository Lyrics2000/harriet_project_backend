# Generated by Django 3.2.8 on 2021-10-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]