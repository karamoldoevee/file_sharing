from django import template

register = template.Library()


@register.filter
def is_private(file, user):
    return user.privates.filter(file=file).count() > 0
