# Generated by Django 4.0.3 on 2022-03-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0012_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='paragraphs',
            field=models.ManyToManyField(to='Acms.container'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
