# Generated by Django 3.2.9 on 2021-11-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0006_page_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='flex_RC',
            field=models.CharField(blank=True, choices=[('row', 'column')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='height',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
    ]
