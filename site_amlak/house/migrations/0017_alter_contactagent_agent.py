# Generated by Django 5.0.7 on 2024-08-28 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0006_agent_telegram'),
        ('house', '0016_contactagent_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactagent',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='agent.agent', verbose_name='مشاور ملک'),
        ),
    ]
