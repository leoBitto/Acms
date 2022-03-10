# Generated by Django 4.0.3 on 2022-03-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0014_article_topic_alter_article_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='url',
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]