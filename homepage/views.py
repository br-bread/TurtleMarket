import json

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/index.html'
    items = Item.objects.published().filter(is_on_main=True)
    texts = [json.loads(item.text.json_string)['html'] for item in items]
    context = {
        'items': items,
        'texts': texts,
        'is_item_list': False,
        'is_item_detail': False,
    }
    return render(request, template_name, context)
