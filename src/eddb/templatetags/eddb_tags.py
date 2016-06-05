# -*- coding: utf-8 -*-

from django import template

register = template.Library()


class RepeatNode(template.Node):
    """
    Repeats its content several times.
    """
    def __init__(self, nodelist, count):
        self.nodelist = nodelist
        self.count = template.Variable(count)

    def render(self, context):
        single_output = self.nodelist.render(context)

        try:
            repetitions = int(self.count.resolve(context))
        except template.VariableDoesNotExist:
            repetitions = 0

        return "".join(single_output for _ in range(repetitions))


@register.tag(name="repeat")
def on_repeat(parser, token):
    """
    Repeats the contained nodelist several times.

    The nodelist is only rendered once and then repeated.
    (i.e. it won't rerender the nodelist on every pass)

    >>> from django.template import Template, Context
    >>> tpl = Template('''{% repeat 4 %} x {% endrepeat %}''')
    >>> tpl.render(Context())
    ... " x  x  x  x  x "
    """
    try:
        tag_name, repetitions = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires 1 argument (number of repetitions)" % token.contents.split()[0])

    nodelist = parser.parse(("endrepeat",))
    parser.delete_first_token()
    return RepeatNode(nodelist, repetitions)


@register.inclusion_tag("eddb/grade_inline.html", name="display_grade")
def on_display_grade(grade):
    """
    Helper tag for rendering grade information in a consistent way -- allows us to change the look and feel in one
    central place.

    :param grade: a numeric value, representing a grade of quality (1..5 usually)
    :return: the rendered display format
    """
    return {
        'grade' : grade,
    }
