from django import template
import datetime
import time

register = template.Library()


@register.filter
def format_date(value):
    time_now = time.time()
    delta = float(time_now) - float(value)
    if delta < 600:
        return "Только что"
    elif delta >= 600 and delta < 86400:
        return f'{round(delta/3600)} часов назад'
    else:
        return datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d')


@register.filter
def format_score(value=None):
    if int(value) <= -5:
        return "Плохая репутация"
    elif int(value)in range(-5, 5):
        return "Нейтральная репутация"
    elif int(value) > 5:
        return "Хорошая репутация"
    else:
        return "Неизвестная репутация"


@register.filter
def format_num_comments(value):
    if int(value) == 0:
        return "Оставьте комментарий"
    elif int(value) in range(0, 51):
        return value
    else:
        return "50+"



@register.filter
def format_selfcomments(message, count):
    if message:
        message_words = message.split(' ')
        return f'{" ".join(message_words[:count])}...{" ".join(message_words[:-1-count:-1])}'
    return "Нет мообщения"