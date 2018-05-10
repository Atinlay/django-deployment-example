from django import template

register = template.Libary()

def cut(value, arg):
    return value.replace(arg, '')

register.filter('cut', cut)
