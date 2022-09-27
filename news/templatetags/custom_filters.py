from django import template
import re

register = template.Library()


@register.filter()
def censor(value):
    bad_words = ['пиздец', 'рис', 'демократичное']
    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")
    for word in re.split(",| ", value):
        if word.lower() in bad_words:
            value = value.replace(word, f'{word[0]}{"*" * (len(word)-1)}')
    return value

