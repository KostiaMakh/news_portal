# Generated by Django 4.0.4 on 2022-05-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_is_published_alter_author_biography_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='', verbose_name='Описание категории'),
        ),
    ]