# Generated by Django 3.2.9 on 2021-12-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0004_auto_20211227_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='logo',
            field=models.ManyToManyField(to='Acms.Image'),
        ),
        migrations.RemoveField(
            model_name='footer',
            name='text_l',
        ),
        migrations.AddField(
            model_name='footer',
            name='text_l',
            field=models.ManyToManyField(related_name='left_text', to='Acms.Text'),
        ),
        migrations.RemoveField(
            model_name='footer',
            name='text_r',
        ),
        migrations.AddField(
            model_name='footer',
            name='text_r',
            field=models.ManyToManyField(related_name='right_text', to='Acms.Text'),
        ),
    ]