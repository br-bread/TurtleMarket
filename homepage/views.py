import json

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/index.html'
    items = (Item.objects
                 .select_related('category')
                 .prefetch_related('tags')
                 .filter(is_published=True)
                 .order_by('name')
                 .only('name', 'text', 'category__name'))
    texts = [json.loads(item.text.json_string)['html'] for item in items]
    context = {
        'items': items,
        'texts': texts,
    }
    return render(request, template_name, context)
