# Generated by Django 3.2.9 on 2022-02-11 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0028_auto_20220210_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grid',
            options={},
        ),
        migrations.RemoveField(
            model_name='grid',
            name='containers',
        ),
        migrations.AddField(
            model_name='container',
            name='grid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.grid'),
        ),
    ]