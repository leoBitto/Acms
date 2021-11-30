from django.db import models
# this block define the graphical part of a block
# the blocks that are rendered need to inherit from
# this class
class BlockGraphic(models.Model):
    width = models.IntegerField(null=True, blank=True, default=100)
    height = models.IntegerField(null=True, blank=True, default=100)
    flex_RC = models.CharField(
                    choices=[
                            ('row', 'row'),
                            ('column','column')
                            ],
                                blank=True,
                                null=True, 
                                max_length=20
                            )
    flex_grow = models.IntegerField(null=True, blank=True, default=1)
    padding = models.IntegerField(null=True, blank=True, default=0)
    margin = models.IntegerField(null=True, blank=True, default=0)
    
    position = models.CharField(
                    choices=[
                            ('top', 'fixed-top'),
                            ('bottom','fixed-bottom'),
                            ('sticky-top','sticky-top'),
                            ('',''),
                            ],
                                blank=True,
                                null=True, 
                                max_length=20
                            )

    top = models.IntegerField(null=True, blank=True, default=0)
    left = models.IntegerField(null=True, blank=True, default=0)
    down = models.IntegerField(null=True, blank=True, default=0)
    right = models.IntegerField(null=True, blank=True, default=0)
    position = models.CharField(
        choices=[
            ('relative','relative'),
            ('absolute','absolute'),
            ('fixed','fixed'),
            ('static','static'),
            ],
        max_length=50,
        blank=True, 
        null=True,
        default="top"
        )

    class Meta:
        abstract = True

    