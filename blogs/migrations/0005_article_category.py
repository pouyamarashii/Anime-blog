# Generated by Django 4.1.2 on 2022-11-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_category_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Category',
            field=models.ManyToManyField(to='blogs.category', verbose_name='دسته بندی'),
        ),
    ]
