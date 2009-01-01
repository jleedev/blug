from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown import markdown
from smartypants import smartyPants as smartypants

register = template.Library()

@register.filter(name='markdown')
@stringfilter
def md(value):
	return mark_safe(markdown(value))
md.is_safe = True

@register.filter(name='smartypants')
@stringfilter
def sp(value):
	return mark_safe(smartypants(value))
sp.is_safe = True
