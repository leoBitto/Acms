# Generated by Django 3.2.9 on 2022-02-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0030_grid_gap'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='cell_min',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='gap',
            field=models.CharField(max_length=10, null=True),
        ),
    ]