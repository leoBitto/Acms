# Generated by Django 3.2.9 on 2021-12-19 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0007_auto_20211219_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='position',
        ),
        migrations.AddField(
            model_name='text',
            name='col',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.col'),
        ),
        migrations.AddField(
            model_name='text',
            name='container',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.container'),
        ),
    ]