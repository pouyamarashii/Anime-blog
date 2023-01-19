# Generated by Django 4.1.2 on 2023-01-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_article_display_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video_title',
            field=models.CharField(max_length=200, null=True, verbose_name='متن زیر ویدیو'),
        ),
        migrations.AlterField(
            model_name='article',
            name='display_video',
            field=models.FileField(default=True, upload_to='video/%y', verbose_name='ویدیو ی پست'),
        ),
    ]
