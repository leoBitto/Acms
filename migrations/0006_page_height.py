# Generated by Django 3.2.9 on 2021-11-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0005_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='height',
            field=models.IntegerField(blank=True, default=400, null=True),
        ),
    ]