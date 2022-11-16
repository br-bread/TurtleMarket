import json

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/index.html'
    items = Item.objects.published().filter(is_on_main=True)
    context = {
        'items': items,
    }
    return render(request, template_name, context)
