from django.db import models
from django.forms import ModelForm, FileField, ClearableFileInput
from ..abstract.abstract import CSS

class Image(CSS):

    #content 
    url = models.FileField(upload_to='', null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    object_fit = models.CharField(
        choices=[
            ('contain', 'contain'),
            ('cover', 'cover'),
            ('fill', 'fill'),
            ('none', 'none'),
            ('scale-down', 'scale-down'),
        ],
        blank=True,
        null=True,
        default='none',
        max_length=15,
    )

    def __str__(self):
        return str(self.url)


