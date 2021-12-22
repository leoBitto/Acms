from django.db import models

class CSS(models.Model):
    # this block define the graphical part of a block
    # the blocks that are rendered need to inherit from
    # this class
    width = models.IntegerField(
        null=True, 
        blank=True, 
        default=100,
        help_text="<h1>you need to put the percentage </h1>",
        )
    height = models.IntegerField(
        null=True, 
        blank=True, 
        default=100,
        help_text="<h1>you need to put the percentage </h1>",
        )
    padding = models.CharField(
        choices=[
            ('-0','0'),
            ('-1','1'),
            ('-2','2'),
            ('-3','3'),
            ('-4','4'),
            ('-5','5'),
            ('-auto','auto'),
        ],
        max_length=5,
        null=True, 
        blank=True, 
        default=0
        )
    margin = models.CharField(
        choices=[
            ('-0','0'),
            ('-1','1'),
            ('-2','2'),
            ('-3','3'),
            ('-4','4'),
            ('-5','5'),
            ('-auto','auto'),
        ],
        max_length=5,
        null=True, 
        blank=True, 
        default=0
        )
    breakpoint = models.CharField(
        max_length=10,
        choices=[
            ('-sm','sm'),
            ('-md','md'),
            ('-lg','lg'),
            ('-xl','xl'),
            ('-xxl','xxl'),
            ('-fluid','fluid'),
            ('', 'no breakpoint')
        ],
        default='',
        blank=True,
        help_text="breakpoint work from the point indicated forward meaning that the content is 100percent until the breakpoint"
        )
    bg_color = models.CharField(
        blank=True,
        null=True,
        max_length=15,
        choices=[
            ('bg-primary','blue'),
            ('bg-secondary','grey'),
            ('bg-success','green'),
            ('bg-danger','red'),
            ('bg-warning','yellow'),
            ('bg-info','lightblue'),
            ('bg-light','light'),
            ('bg-dark','dark'),
            ('bg-body','body'),
            ('bg-white','white'),
            ('bg-transparent','transparent'),
            ('','no bg color'),
            ],
        )
    bg_gradient = models.BooleanField(
        default=False, 
        blank=True, 
        null=True
        )
    position = models.CharField(
                    choices=[
                            ('position-static', 'static'),
                            ('position-relative', 'relative'),
                            ('position-absolute', 'absolute'),
                            ('position-fixed', 'fixed'),
                            ('position-sticky', 'sticky'),
                            
                            ],
                                blank=True,
                                null=True, 
                                max_length=20
                            )
    top = models.IntegerField(
        null=True, 
        blank=True, 
        default=''
        )
    left = models.IntegerField(
        null=True, 
        blank=True, 
        default=''
        )
    down = models.IntegerField(
        null=True, 
        blank=True, 
        default=''
        )
    right = models.IntegerField(
        null=True, 
        blank=True, 
        default=''
        )
    display = models.CharField(
        choices=[
            ('-none','none'),
            ('-inline','inline'),
            ('-block','block'),
            ('-flex','flex'),
            ],
        max_length=50,
        blank=True, 
        null=True,
        default="",
        )

    class Meta:
        abstract = True


class Flex(CSS):
    direction = models.CharField(
        choices=[
            ('column','column'),
            ('column-reverse','column-reverse'),
            ('row','row'),
            ('row-reverse','row-reverse'),
        ],
        default='',
        blank=True,
        max_length=20,
        )   
    justify_content = models.CharField(
        max_length=10,
        choices=[
            ('-start','start'),
            ('-center','center'),
            ('-end','end'),
            ('-around','around'),
            ('-between','between'),
            ('-evenly','evenly'),
        ],
        default='',
        blank=True,
        )   
    align_items = models.CharField(
        max_length=10,
        choices=[
            ('-start','start'),
            ('-center','center'),
            ('-end','end'),
            ('-baseline','baseline'),
            ('-stretch','stretch'),
        ],
        default='',
        blank=True,
        )
    align_self = models.CharField(
        max_length=10,
        choices=[
            ('-start','start'),
            ('-center','center'),
            ('-end','end'),
            ('-baseline','baseline'),
            ('-stretch','stretch'),
        ],
        default='',
        blank=True,
        )
    align_content = models.CharField(
        max_length=10,
        choices=[
            ('-start','start'),
            ('-center','center'),
            ('-end','end'),
            ('-around','around'),
            ('-stretch','stretch'),
        ],
        default='',
        blank=True,
        )
    
    flex_grow = models.IntegerField(
        default=1,
        blank=True,
        )

    class Meta:
        abstract = True

