# Generated by Django 5.0.7 on 2024-08-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_alter_house_house_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='first_photo',
            field=models.ImageField(upload_to='house/', verbose_name='تصویر شاخص'),
        ),
        migrations.AlterField(
            model_name='house',
            name='second_photo',
            field=models.ImageField(blank=True, null=True, upload_to='house/', verbose_name='تصویر دوم'),
        ),
        migrations.AlterField(
            model_name='house',
            name='third_photo',
            field=models.ImageField(blank=True, null=True, upload_to='house/', verbose_name='تصویر سوم'),
        ),
    ]
