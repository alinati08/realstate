# Generated by Django 5.0.7 on 2024-08-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_rename_photo_house_first_photo_house_aria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_park',
            field=models.CharField(choices=[('yes', ' دارد '), ('no', ' ندارد  ')], default='no', max_length=10, verbose_name=' : وضعیت پارکینگ '),
        ),
        migrations.AlterField(
            model_name='house',
            name='second_photo',
            field=models.ImageField(blank=True, null=True, upload_to='house/'),
        ),
        migrations.AlterField(
            model_name='house',
            name='third_photo',
            field=models.ImageField(blank=True, null=True, upload_to='house/'),
        ),
    ]
