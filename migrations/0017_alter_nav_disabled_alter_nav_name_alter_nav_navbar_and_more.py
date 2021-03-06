# Generated by Django 4.0.3 on 2022-03-14 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0016_nav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav',
            name='disabled',
            field=models.CharField(blank=True, choices=[('disabled', 'disabled'), ('', 'active')], default='', help_text='if disabled the link is shown as greyish', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nav',
            name='name',
            field=models.CharField(blank=True, help_text='the string shown in the navbar', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nav',
            name='navbar',
            field=models.ForeignKey(blank=True, help_text='the navbar the nav belongs to', null=True, on_delete=django.db.models.deletion.CASCADE, to='Acms.navbar'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='order',
            field=models.IntegerField(help_text='the order the nav has'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='url_toPage',
            field=models.CharField(blank=True, help_text='the url that the page has    its not a page to avoid circular import', max_length=50, null=True),
        ),
    ]
