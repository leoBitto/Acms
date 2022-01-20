# Generated by Django 3.2.9 on 2021-12-28 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0008_auto_20211228_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='container',
            old_name='section',
            new_name='sections',
        ),
        migrations.RemoveField(
            model_name='image',
            name='display',
        ),
        migrations.RemoveField(
            model_name='section',
            name='pages',
        ),
        migrations.AddField(
            model_name='section',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.page'),
        ),
        migrations.AlterField(
            model_name='container',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='container',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='container',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='container',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='container',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='footer',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='footer',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='footer',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='footer',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='footer',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='image',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='link',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='link',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='link',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='link',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='overlay',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='overlay',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='overlay',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='overlay',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='overlay',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='section',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='section',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='section',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='section',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='text',
            name='align_self',
            field=models.CharField(choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10),
        ),
        migrations.AlterField(
            model_name='text',
            name='breakpoint',
            field=models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), ('', 'no breakpoint')], default='', help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10),
        ),
        migrations.AlterField(
            model_name='text',
            name='display',
            field=models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='text',
            name='order',
            field=models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='text',
            name='position',
            field=models.CharField(choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20),
        ),
    ]