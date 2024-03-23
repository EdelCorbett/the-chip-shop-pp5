from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg