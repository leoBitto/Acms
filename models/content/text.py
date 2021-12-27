from django.db import models
from ..abstract.abstract import CSS


class Text(CSS):

    #content 
    txt = models.TextField(null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    color = models.CharField(
            choices=[
                ('-primary','blue'),
                ('-secondary','grey'),
                ('-success','green'),
                ('-danger','red'),
                ('-warning','yellow'),
                ('-info','lightblue'),
                ('-light','light'),
                ('-dark','dark'),
                ('-body','body'),
                ('-muted','muted'),
                ('-white','white'),
                ('-black','black'),
            ],
            max_length=25,
            blank=True,
            null=True,
        )
    font = ...
    overflow = models.CharField(
            choices=[
                ('-auto','auto'),
                ('-hidden','hidden'),
                ('-visible','visible'),
                ('-scroll','scroll'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )
    alignment = models.CharField(
            choices=[
                ('-start','start'),
                ('-center','center'),
                ('-end','end'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )
    size = models.CharField(
            choices=[
                ('-1','1'),
                ('-2','2'),
                ('-3','3'),
                ('-4','4'),
                ('-5','5'),
                ('-6','6'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )
    weight = models.CharField(
            choices=[
                ('-bold','bold'),
                ('-bolder','bolder'),
                ('-normal','normal'),
                ('-light','light'),
                ('-lighter','lighter'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )
    italics = models.CharField(
            choices=[
                ('-italic','italic'),
                ('-normal','normal'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )
    line_height = models.CharField(
            choices=[
                ('-sm','small'),
                ('-base','normal'),
                ('-lg','large'),
            ],
            max_length=5,
            blank=True,
            null=True,
        )
    text_decoration = models.CharField(
            choices=[
                ('-underline','underline'),
                ('-line-through','line through'),
                ('-none','none'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )
    vertical_align = models.CharField(
            choices=[
                ('-baseline','baseline'),
                ('-top','top'),
                ('-middle','middle'),
                ('-bottom','bottom'),
                ('-text-top','text-top'),
                ('-text-bottom','text-bottom'),
            ],
            max_length=15,
            blank=True,
            null=True,
        )

    def __str__(self):
        return self.txt[:15]