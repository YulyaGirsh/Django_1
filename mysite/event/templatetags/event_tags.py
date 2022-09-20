from event.models import *
from django import template

register = template.Library()


@register.simple_tag()
def get_area(filter=None):
    if not filter:
        return Area.objects.all()
    else:
        return Area.objects.filter(pk=filter)


@register.inclusion_tag('event/list_areas.html')
def show_areas(sort=None, area_selected=0):
    if not sort:
        area = Area.objects.all()
    else:
        area = Area.objects.order_by(sort)
    return {"area": area, "area_selected": area_selected}
