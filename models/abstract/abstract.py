############################################################
############################################################

##     model name: CSS                    
##     superclass: models.Model
##     subclass:   
#           Flex
##     points to:
##     abstract: Yes 

##     description:
#            it have a lot the caracteristics that bootstrap5
#            allow to control plus strings to add custom 
#            classes and id to objects displayed
#           
#           
#            
#           
#            
#           

##     parameters:
#           CSS_id
    #       CSS_classes
    #       width
    #       height    
    #       col

    #       padding_sides
    #       padding 
    #       margin_sides
    #       margin
    
    #       breakpoint
    #       bg_image
    #       bg_color
    #       bg_gradient
    
    #       borders to be implemented..

    #       shadows
    #       position
    #       top 
    #       left
    #       down 
    #       right 
    #       order 
    #       align_self 
    #       visibility
    #       display     
    
##       methods:
#           

####    Admin stuff

##    set of params:
#           html_tags
#           sizes
#           spacing
#           background
#           position
#           misc
#                 


############################################################
############################################################
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
    width = models.CharField( 
        blank=True, 
        null=True,
        default='',
        max_length=10,
        )
    height = models.CharField( 
        blank=True, 
        null=True,
        default='',
        max_length=10,
        )
    
    #bootstrap sizing
    col = models.CharField(
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
            ('7','7'),
            ('8','8'),
            ('9','9'),
            ('10','10'),
            ('11','11'),
            ('12','12'),
        ],
        max_length=3, 
        blank=True, 
        null=True,
        default=''
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
        default='-0'
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
        default='-0'
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
        null=True,
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
            ('bg-gradient','bottom-top gradient'),
            ('','no gradient'),
        ],
        default='', 
        blank=True, 
        max_length=20,
        )
    
    #borders
    borders = models.CharField(
            choices = [
                ('rounded', 'small rounding all corners'),
                ('rounded-top', 'small rounding top corners'),
                ('rounded-end', 'small rounding right corners'),
                ('rounded-bottom', 'small rounding bottom corners'),
                ('rounded-start', 'small rounding left corners'),
                ('rounded-circle', 'as a circle'),
                ('rounded-pill', 'in pill form'),
                ('', 'no rounding'),
            ],
            default = '',
            blank = True,
            null = True,
            max_length=30,
    )

    #borders colors
    borders_colors = models.CharField(
            choices = [
                ('border border-primary', 'blue'),
                ('border border-secondary', 'grey'),
                ('border border-success', 'green'),
                ('border border-danger', 'red'),
                ('border border-warning', 'yellow'),
                ('border border-info', 'cyan'),
                ('border border-light', 'light'),
                ('border border-dark', 'black'),
                ('border border-white', 'white '),
                ('', 'no border, no color'),
            ],
            default = '',
            blank = True,
            null = True,
            max_length=30,
        )

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
                            ('','no specified position'),
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
        blank=False, 
        default='order-0',
        max_length=10,
        )
    align_self = models.CharField(
        max_length=10,
        choices=[
            ('-start','start'),
            ('-center','center'),
            ('-end','end'),
            ('-baseline','baseline'),
            ('-stretch','stretch'),
            ('','no value'),
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
    opacity = models.CharField(
        max_length=10,
        choices=[
            ('-0','0'),
            ('-25','25'),
            ('-50','50'),
            ('-75','75'),
            ('-100','100'),  
        ],
        default='-100',
        blank=True,
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
        blank=False, 
        default="-flex",
        )

    class Meta:
        abstract = True


############################################################
############################################################

##     model name: Flex                    
##     superclass: CSS
##     subclass:   
#           Section
##     points to:
##     abstract: Yes 

##     description:
#            it have a lot the caracteristics that bootstrap5
#            allow to control regardin the flex properties       
#           

##     parameters:
#           +CSS
#           inline
#           direction
#           flex-wrap
#           justify-content
#           align-items
#           align-content
#           flex-grow  
    
##       methods:
#           

####    Admin stuff

##    set of params:
#           flex_properties
#           
#


############################################################
############################################################


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
        default='row',
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
        default='-nowrap',
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
        default='-center',
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
        default='-center',
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
        default='-center',
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

