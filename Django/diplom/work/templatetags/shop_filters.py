from django import template

register = template.Library()

@register.filter
def format_review(value: int):
    return '★' * value