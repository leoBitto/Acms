# Generated by Django 3.2.9 on 2022-02-10 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acms', '0027_overlay_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CSS_id', models.CharField(blank=True, default='', help_text='set id of div', max_length=50)),
                ('CSS_classes', models.TextField(blank=True, default='', help_text='additional css classes')),
                ('width', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('height', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('col', models.CharField(blank=True, choices=[('-1', '1'), ('-2', '2'), ('-3', '3'), ('-4', '4'), ('-5', '5'), ('-6', '6'), ('-7', '7'), ('-8', '8'), ('-9', '9'), ('-10', '10'), ('-11', '11'), ('-12', '12')], default='', max_length=3, null=True)),
                ('padding_sides', models.CharField(blank=True, choices=[('t', 'top'), ('b', 'bottom'), ('s', 'left'), ('e', 'right'), ('x', 'left and right'), ('y', 'top and bottom'), ('', 'all margins')], default='', max_length=5)),
                ('padding', models.CharField(blank=True, choices=[('-0', '0'), ('-1', '1'), ('-2', '2'), ('-3', '3'), ('-4', '4'), ('-5', '5'), ('-auto', 'auto')], default='', max_length=5, null=True)),
                ('margin_sides', models.CharField(blank=True, choices=[('t', 'top'), ('b', 'bottom'), ('s', 'left'), ('e', 'right'), ('x', 'left and right'), ('y', 'top and bottom'), ('', 'all margins')], default='', max_length=5)),
                ('margin', models.CharField(blank=True, choices=[('-0', '0'), ('-1', '1'), ('-2', '2'), ('-3', '3'), ('-4', '4'), ('-5', '5'), ('-auto', 'auto')], default='', max_length=5, null=True)),
                ('breakpoint', models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), (None, 'no breakpoint')], default=None, help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10, null=True)),
                ('bg_image', models.ImageField(blank=True, default='', upload_to='')),
                ('bg_color', models.CharField(blank=True, choices=[('bg-primary', 'blue'), ('bg-secondary', 'grey'), ('bg-success', 'green'), ('bg-danger', 'red'), ('bg-warning', 'yellow'), ('bg-info', 'lightblue'), ('bg-light', 'light'), ('bg-dark', 'dark'), ('bg-body', 'body'), ('bg-white', 'white'), ('bg-transparent', 'transparent'), ('', 'no bg color')], default='', max_length=15)),
                ('bg_gradient', models.CharField(blank=True, choices=[('.bg-gradient', 'bottom-top gradient'), ('', 'no gradient')], default='', max_length=20)),
                ('shadow', models.CharField(blank=True, choices=[('shadow-sm', 'small shadow'), ('shadow', 'normal shadow'), ('shadow-lg', 'large shadow'), ('', 'no value')], default='', max_length=20)),
                ('position', models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20)),
                ('top', models.IntegerField(blank=True, default=0, null=True)),
                ('left', models.IntegerField(blank=True, default=0, null=True)),
                ('down', models.IntegerField(blank=True, default=0, null=True)),
                ('right', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10)),
                ('align_self', models.CharField(blank=True, choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch'), ('', 'no value')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10)),
                ('visibility', models.CharField(blank=True, choices=[('visible', 'visible'), ('invisible', 'invisible'), ('', 'no value')], default='', max_length=15)),
                ('opacity', models.CharField(blank=True, choices=[('-0', '0'), ('-25', '25'), ('-50', '50'), ('-75', '75'), ('-100', '100')], default='', max_length=10)),
                ('display', models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='-flex', max_length=50)),
                ('name', models.CharField(blank=True, max_length=10)),
                ('inside_text', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CSS_id', models.CharField(blank=True, default='', help_text='set id of div', max_length=50)),
                ('CSS_classes', models.TextField(blank=True, default='', help_text='additional css classes')),
                ('width', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('height', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('col', models.CharField(blank=True, choices=[('-1', '1'), ('-2', '2'), ('-3', '3'), ('-4', '4'), ('-5', '5'), ('-6', '6'), ('-7', '7'), ('-8', '8'), ('-9', '9'), ('-10', '10'), ('-11', '11'), ('-12', '12')], default='', max_length=3, null=True)),
                ('padding_sides', models.CharField(blank=True, choices=[('t', 'top'), ('b', 'bottom'), ('s', 'left'), ('e', 'right'), ('x', 'left and right'), ('y', 'top and bottom'), ('', 'all margins')], default='', max_length=5)),
                ('padding', models.CharField(blank=True, choices=[('-0', '0'), ('-1', '1'), ('-2', '2'), ('-3', '3'), ('-4', '4'), ('-5', '5'), ('-auto', 'auto')], default='', max_length=5, null=True)),
                ('margin_sides', models.CharField(blank=True, choices=[('t', 'top'), ('b', 'bottom'), ('s', 'left'), ('e', 'right'), ('x', 'left and right'), ('y', 'top and bottom'), ('', 'all margins')], default='', max_length=5)),
                ('margin', models.CharField(blank=True, choices=[('-0', '0'), ('-1', '1'), ('-2', '2'), ('-3', '3'), ('-4', '4'), ('-5', '5'), ('-auto', 'auto')], default='', max_length=5, null=True)),
                ('breakpoint', models.CharField(choices=[('-sm', 'sm'), ('-md', 'md'), ('-lg', 'lg'), ('-xl', 'xl'), ('-xxl', 'xxl'), ('-fluid', 'fluid'), (None, 'no breakpoint')], default=None, help_text='breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint', max_length=10, null=True)),
                ('bg_image', models.ImageField(blank=True, default='', upload_to='')),
                ('bg_color', models.CharField(blank=True, choices=[('bg-primary', 'blue'), ('bg-secondary', 'grey'), ('bg-success', 'green'), ('bg-danger', 'red'), ('bg-warning', 'yellow'), ('bg-info', 'lightblue'), ('bg-light', 'light'), ('bg-dark', 'dark'), ('bg-body', 'body'), ('bg-white', 'white'), ('bg-transparent', 'transparent'), ('', 'no bg color')], default='', max_length=15)),
                ('bg_gradient', models.CharField(blank=True, choices=[('.bg-gradient', 'bottom-top gradient'), ('', 'no gradient')], default='', max_length=20)),
                ('shadow', models.CharField(blank=True, choices=[('shadow-sm', 'small shadow'), ('shadow', 'normal shadow'), ('shadow-lg', 'large shadow'), ('', 'no value')], default='', max_length=20)),
                ('position', models.CharField(blank=True, choices=[('position-static', 'static'), ('position-relative', 'relative'), ('position-absolute', 'absolute'), ('position-fixed', 'fixed'), ('position-sticky', 'sticky'), ('', 'no specified position')], default='', max_length=20)),
                ('top', models.IntegerField(blank=True, default=0, null=True)),
                ('left', models.IntegerField(blank=True, default=0, null=True)),
                ('down', models.IntegerField(blank=True, default=0, null=True)),
                ('right', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.CharField(choices=[('order-0', '0'), ('order-1', '1'), ('order-2', '2'), ('order-3', '3'), ('order-4', '4'), ('order-5', '5'), ('', 'no order')], default='order-0', max_length=10)),
                ('align_self', models.CharField(blank=True, choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch'), ('', 'no value')], default='', help_text='\n            align the item on the\n            vertical axis in a flex container\n        ', max_length=10)),
                ('visibility', models.CharField(blank=True, choices=[('visible', 'visible'), ('invisible', 'invisible'), ('', 'no value')], default='', max_length=15)),
                ('opacity', models.CharField(blank=True, choices=[('-0', '0'), ('-25', '25'), ('-50', '50'), ('-75', '75'), ('-100', '100')], default='', max_length=10)),
                ('display', models.CharField(choices=[('-none', 'none'), ('-inline', 'inline'), ('-block', 'block'), ('-flex', 'flex')], default='-flex', max_length=50)),
                ('inline', models.CharField(blank=True, choices=[('', 'not inline'), ('-inline', 'inline')], default='', max_length=10)),
                ('direction', models.CharField(blank=True, choices=[('column', 'column'), ('column-reverse', 'column-reverse'), ('row', 'row'), ('row-reverse', 'row-reverse')], default='', max_length=20)),
                ('flex_wrap', models.CharField(blank=True, choices=[('-wrap', 'wrap'), ('-nowrap', 'no wrap'), ('-wrap-reverse', 'wrap reverse')], default='', help_text='\n            wrap of the content inside flex container\n            in one row if no wrap\n            in multiple rows in wrap\n            multiple rows from bottom in wrap reverse\n        ', max_length=15)),
                ('justify_content', models.CharField(blank=True, choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-around', 'around'), ('-between', 'between'), ('-evenly', 'evenly')], default='', help_text='\n            alignment of content on the main axis:\n            x if direction is row;\n            y if direction is column.\n        ', max_length=10)),
                ('align_items', models.CharField(blank=True, choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-baseline', 'baseline'), ('-stretch', 'stretch')], default='', help_text='\n            alignment of content on the cross axis:\n            y if direction is row;\n            x if direction is column.\n        ', max_length=10)),
                ('align_content', models.CharField(blank=True, choices=[('-start', 'start'), ('-center', 'center'), ('-end', 'end'), ('-around', 'around'), ('-stretch', 'stretch')], default='', help_text='\n            align all the  content\n            on the cross axis if there is space \n        ', max_length=10)),
                ('flex_grow', models.IntegerField(blank=True, default=1, help_text='\n        \n        ', null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('containers', models.ManyToManyField(to='Acms.Container')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.section')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='overlay',
            name='button',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Acms.button'),
        ),
    ]
