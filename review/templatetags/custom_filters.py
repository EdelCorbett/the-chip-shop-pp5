from django import template

register = template.Library()


@register.filter
def star_range(value):
    if value is None:
        return range(0)
    else:
        return range(1, int(value) + 1)