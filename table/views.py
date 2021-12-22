from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def index(request):
    contentdata = item.objects.all()
    per_page = 4
    obj_paginator = Paginator(contentdata, per_page)
    items = obj_paginator.page(1).object_list
    page_range = obj_paginator.page_range
    context = {
        'obj_paginator': obj_paginator,
        'items': items,
        'page_range': page_range,
        'fields': item._meta.get_fields()
    }

    if request.method == 'POST':
        page_no = request.POST.get('page_no', None)
        items = obj_paginator.page(page_no).object_list
        context = {
            'obj_paginator': obj_paginator,
            'items': items,
            'fields': item._meta.get_fields()
        }
        return render(request, 'table.html', context)

    return render(request, 'base.html', context)


def filter_table(request):
    field = request.GET.get('field')
    condit = request.GET.get('condit')
    filter = request.GET.get('filter')
    field_filter = {}
    if condit == 'Равно':
        field_filter[field] = filter
    if condit == 'Содержит':
        field += '__icontains'
        field_filter[field] = filter
    if condit == 'Больше':
        field += '__gt'
        field_filter[field] = filter
    if condit == 'Меньше':
        field += '__lt'
        field_filter[field] = filter
    items = item.objects.all().filter(**field_filter)
    return render(request, 'table.html', context={'items': items, 'fields': item._meta.get_fields()})