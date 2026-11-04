
from django import template
from client.models import specialization , Area

register = template.Library()

@register.simple_tag
def get_specializations():
    return specialization.objects.all()

@register.simple_tag
def get_areas():
    return Area.objects.all()