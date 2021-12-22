# Generated by Django 3.2.9 on 2021-12-20 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0013_auto_20211220_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='col',
            name='down',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='col',
            name='left',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='col',
            name='position',
            field=models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='col',
            name='right',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='col',
            name='top',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='down',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='left',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='position',
            field=models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='right',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='top',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='down',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='left',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='position',
            field=models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='right',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='top',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='down',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='left',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='right',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='top',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='down',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='left',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='position',
            field=models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='right',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='top',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='down',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='left',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='right',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='top',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.CreateModel(
            name='Overlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakpoint', models.CharField(blank=True, choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10)),
                ('bg_color', models.CharField(blank=True, choices=[('bg-primary', 'blue'), ('bg-secondary', 'grey'), ('bg-success', 'green'), ('bg-danger', 'red'), ('bg-warning', 'yellow'), ('bg-info', 'lightblue'), ('bg-light', 'light'), ('bg-dark', 'dark'), ('bg-body', 'body'), ('bg-white', 'white'), ('bg-transparent', 'transparent'), ('', 'no bg color')], max_length=15, null=True)),
                ('bg_gradient', models.BooleanField(blank=True, default=False, null=True)),
                ('down', models.IntegerField(blank=True, default='', null=True)),
                ('right', models.IntegerField(blank=True, default='', null=True)),
                ('display', models.CharField(blank=True, choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50, null=True)),
                ('toPage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]