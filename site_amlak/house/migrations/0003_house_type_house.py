# Generated by Django 5.0.7 on 2024-07-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_alter_house_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='type_house',
            field=models.CharField(choices=[('اجاره', 'R'), ('فروش', 'S')], default='S', max_length=10, verbose_name='نوع فروش '),
        ),
    ]
