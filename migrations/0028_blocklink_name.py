# Generated by Django 3.2.9 on 2021-11-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0027_auto_20211129_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocklink',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]