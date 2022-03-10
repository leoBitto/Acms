# Generated by Django 4.0.3 on 2022-03-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0013_alter_article_paragraphs_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]