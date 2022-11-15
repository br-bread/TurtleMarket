import json

from django.shortcuts import get_object_or_404, render

from catalog.models import Item, MainImage


def item_list(request):
    template_name = 'catalog/index.html'
    items = (Item.objects
                 .select_related('category')
                 .prefetch_related('tags')
                 .filter(is_published=True)
                 .filter(category__is_published=True)
                 .order_by('category__name')
                 .only('name', 'text', 'category__name'))
    texts = [json.loads(item.text.json_string)['html'] for item in items]
    context = {
        'items': items,
        'texts': texts,
        'is_item_list': True,
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
    }
    return render(request, template_name, context)
