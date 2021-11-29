# Generated by Django 3.2.8 on 2021-11-29 03:48

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211129_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurSerices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('header1', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to=mainapp.models.upload_image_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='signature',
        ),
    ]
