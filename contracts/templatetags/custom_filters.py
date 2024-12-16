from django import template

register = template.Library()
@register.filter
def get_field(instance,field_name):
    return getattr(instance, field_name, '')

@register.filter
def to(value):
    try:
        return range(1, value+1)
    except TypeError:
        return []
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, key)