from django import template
register = template.Library()
@register.filter
def multiply(value, arg):
    print(int(value * (arg+100)/100))
    try: 
        return int(value * (arg+100)/100)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0
@register.filter    
def replace_dash_with_slash(value):
    print(type(value))
    try: 
        value = str(value)
        return value.replace('-','/')
    except Exception:
        return value
