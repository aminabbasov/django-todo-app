from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter(name='colorize')
@stringfilter
def colorize(value):
    COLOR_DICT = {
        '7': '#ff000000',
        '0': '#FF0000af',
        '1': '#FF8000af',
        '2': '#FFFF00af',
        '3': '#00DD1Daf',
        '4': '#00FFFFaf',
        '5': '#0084FFaf',
        '6': '#8A2BE2af',
    }

    return COLOR_DICT[value]

# register.filter('colorize', colorize)
