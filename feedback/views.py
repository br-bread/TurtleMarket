from django.shortcuts import render

from . import forms


def feedback(request):
    template_name = 'feedback/index.html'
    form = forms.FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, template_name, context)
