# Generated by Django 5.0.7 on 2024-09-01 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0004_remove_job_company_job_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recruiter.job'),
            preserve_default=False,
        ),
    ]