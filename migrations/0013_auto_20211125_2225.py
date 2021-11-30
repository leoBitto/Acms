# Generated by Django 3.2.9 on 2021-11-25 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0012_blockcontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='section',
        ),
        migrations.AddField(
            model_name='text',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.blockcontent'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('width', models.IntegerField(blank=True, default=100, null=True)),
                ('height', models.IntegerField(blank=True, default=100, null=True)),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.blocksection')),
            ],
        ),
    ]
