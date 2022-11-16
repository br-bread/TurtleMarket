from django.shortcuts import get_object_or_404, render
from catalog.models import Item


def item_list(request):
    template_name = 'catalog/index.html'
    items = Item.objects.published().order_by('category__name')
    context = {
        'items': items,
    }
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'catalog/detail.html'
    item = get_object_or_404(
        Item.objects.filter(is_published=True,
                            category__is_published=True),
        pk=pk
    )
    context = {
        'item': item,
    }
    return render(request, template_name, context)


def handler404(request, exception, template_name="error_404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response
