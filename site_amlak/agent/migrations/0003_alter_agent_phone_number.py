# Generated by Django 5.0.7 on 2024-08-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_agent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, verbose_name='شماره موبایل '),
        ),
    ]
