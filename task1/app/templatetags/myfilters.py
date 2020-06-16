from django import template

register = template.Library()

@register.filter
def vol2color(value):

    # print(float(value))
    if value == '':
        return 'white'
    elif float(value) < 0:
        return 'green'
    elif float(value) >1 and float(value) < 2:
        return 'LightSalmon'
    elif float(value) >=2 and float(value) < 5:
        return 'DarkSalmon'
    elif float(value) >= 5:
        return 'Salmon'
    else:
        return 'white'