import json

from django.shortcuts import get_object_or_404, render
from catalog.models import Item, MainImage


def item_list(request):
    template_name = 'catalog/index.html'
    items = Item.objects.published().order_by('category__name')
    texts = [json.loads(item.text.json_string)['html'] for item in items]
    context = {
        'items': items,
        'texts': texts,
        'is_item_list': True,
        'is_item_detail': False,
    }
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'catalog/detail.html'
    item = get_object_or_404(Item, pk=pk)
    try:
        preview = MainImage.objects.get(item=pk).image_tmb
    except Exception:
        preview = None
    text = json.loads(item.text.json_string)['html']
    context = {
        'item': item,
        'preview': preview,
        'text': text,
        'is_item_list': False,
        'is_item_detail': True,
    }
    return render(request, template_name, context)


def handler404(request, exception, template_name="error_404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response
