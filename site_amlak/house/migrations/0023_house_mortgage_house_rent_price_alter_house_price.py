# Generated by Django 5.0.7 on 2024-08-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0022_alter_contactagent_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='mortgage',
            field=models.IntegerField(null=True, verbose_name='رهن'),
        ),
        migrations.AddField(
            model_name='house',
            name='rent_price',
            field=models.IntegerField(null=True, verbose_name='اجاره '),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(verbose_name='  قیمت  فروش'),
        ),
    ]
