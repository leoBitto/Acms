from django.db import models


class CSS(models.Model):
    
    #meta 
    CSS_id = models.CharField(
        max_length=50, 
        default='',
        blank=True,
        help_text="set id of div"
        )
    CSS_classes = models.TextField(
        blank=True,
        help_text="additional css classes",
        default='',
        )
    # this block define the graphical part of a block
    # the blocks that are rendered need to inherit from
    # this class
    #sizing
    width = models.IntegerField( 
        blank=True, 
        null=True,
        default=100,
        )
    height = models.IntegerField(
        blank=True, 
        null=True,
        default=100,
        )
    
    #Spacing
    padding_sides = models.CharField(
        choices=[
            ('t','top'),
            ('b','bottom'),
            ('s','left'),
            ('e','right'),
            ('x','left and right'),
            ('y','top and bottom'),
            ('','all margins'),
        ],
        max_length=5,
        blank=True,
        default=''
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
        blank=True, 
        null=True,
        default='-auto'
        )
    margin_sides = models.CharField(
        choices=[
            ('t','top'),
            ('b','bottom'),
            ('s','left'),
            ('e','right'),
            ('x','left and right'),
            ('y','top and bottom'),
            ('','all margins'),
        ],
        max_length=5,
        blank=True,
        default=''
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
        blank=True, 
        null=True,
        default='-auto'
        )
    
    #breakpoint
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
    
    #background
    #to avoid circular import we need to define 
    # an image and not point to one
    bg_image = models.ImageField(
        upload_to='',  
        blank=True,
        default='',
        )
    bg_color = models.CharField(
        blank=True,
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
        default='',
        )
    bg_gradient = models.CharField(
        choices=[
            ('.bg-gradient','bottom-top gradient'),
            ('','no gradient'),
        ],
        default='', 
        blank=True, 
        max_length=20,
        )
    
    #borders

    #shadows
    shadow = models.CharField(
            choices=[
                ('shadow-sm','small shadow'),
                ('shadow','normal shadow'),
                ('shadow-lg','large shadow'),
                ('','no value')
            ], 
            blank=True,
            default='',
            max_length=20,
        )

    #position
    position = models.CharField(
                    choices=[
                            ('position-static', 'static'),
                            ('position-relative', 'relative'),
                            ('position-absolute', 'absolute'),
                            ('position-fixed', 'fixed'),
                            ('position-sticky', 'sticky'),
                            
                            ],
                    blank=True, 
                    max_length=20,
                    default='',
                            )
    top = models.IntegerField( 
        blank=True, 
        null=True,
        default=0,
        )
    left = models.IntegerField(
        blank=True,
        null=True,
        default=0, 
        )
    down = models.IntegerField(
        blank=True,
        null=True, 
        default=0,
        )
    right = models.IntegerField(
        blank=True,
        null=True, 
        default=0,
        )

    #flex relative positioning,
    # they work if flex or absolute
    # are active in the position 
    # or display parameters 
    order = models.CharField(
        choices=[
            ('order-0','0'),
            ('order-1','1'),
            ('order-2','2'),
            ('order-3','3'),
            ('order-4','4'),
            ('order-5','5'),
            ('','no order'),
        ],
        blank=True, 
        default='order-0',
        max_length=20,
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
        help_text="""
            align the item on the
            vertical axis in a flex container
        """,
        )

    #visibility
    visibility = models.CharField(
        choices=[
            ('visible', 'visible'),
            ('invisible','invisible'),
            ('', 'no value'),
        ],
        max_length=15,
        blank=True,
        default='',
        )

    #display from utilities
    display = models.CharField(
        choices=[
            ('-none','none'),
            ('-inline','inline'),
            ('-block','block'),
            ('-flex','flex'),
            ],
        max_length=50,
        blank=True, 
        default="",
        )

    class Meta:
        abstract = True


class Flex(CSS):
    inline = models.CharField(
        choices=[
            ('','not inline'),
            ('-inline','inline'),
        ],
        default='',
        blank=True,
        max_length=10,
        )
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
    flex_wrap = models.CharField(
        max_length=15,
        choices=[
            ('-wrap','wrap'),
            ('-nowrap','no wrap'),
            ('-wrap-reverse','wrap reverse'),
        ],
        default='',
        blank=True,
        help_text="""
            wrap of the content inside flex container
            in one row if no wrap
            in multiple rows in wrap
            multiple rows from bottom in wrap reverse
        """,
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
        help_text="""
            alignment of content on the main axis:
            x if direction is row;
            y if direction is column.
        """,
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
        help_text="""
            alignment of content on the cross axis:
            y if direction is row;
            x if direction is column.
        """,
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
        help_text="""
            align all the  content
            on the cross axis if there is space 
        """,
        )

    flex_grow = models.IntegerField(
        default=1,
        blank=True,
        null=True,
        help_text="""
        
        """,
        )

    class Meta:
        abstract = True

