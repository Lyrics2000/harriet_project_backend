# Generated by Django 3.2.8 on 2021-11-29 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_auto_20211129_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowerassets',
            name='loan_proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.loanproposal'),
        ),
        migrations.AddField(
            model_name='employmentdetails',
            name='loan_proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.loanproposal'),
        ),
    ]