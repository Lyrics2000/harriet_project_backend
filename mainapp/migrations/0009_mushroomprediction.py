# Generated by Django 3.2.8 on 2021-12-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211129_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='MushroomPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mushroon_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('mushroom_date_price', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]