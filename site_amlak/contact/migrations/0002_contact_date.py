# Generated by Django 5.0.7 on 2024-08-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ثبت'),
        ),
    ]
