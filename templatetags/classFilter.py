from django import template

register = template.Library()

@register.filter
def classname(self):
        return self.__class__.__name__
