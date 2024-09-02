# Generated by Django 5.0.7 on 2024-07-30 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('sluf', models.SlugField(verbose_name='عنوان لاتین')),
                ('published_at', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.category', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='blogs', to='blog.tag', verbose_name='تگ ها'),
        ),
    ]
