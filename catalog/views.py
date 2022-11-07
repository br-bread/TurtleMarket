from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    template_name = 'catalog/index.html'
    return render(request, template_name, {})


def item_detail(request, pk):
    return HttpResponse(f'Подробно элемент №{pk}')
