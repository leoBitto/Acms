# Generated by Django 4.0.2 on 2022-02-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0005_navbar_has_user_functionality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='brand_name',
            field=models.CharField(blank=True, default='', help_text='this is the name of the brand', max_length=25, null=True),
        ),
    ]
