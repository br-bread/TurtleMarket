from django.core.mail import send_mail
from django.shortcuts import redirect, render

from . import forms
from .models import Feedback


def feedback(request):
    template_name = 'feedback/index.html'
    form = forms.FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        mail = form.cleaned_data['mail']
        feedback_text = form.cleaned_data['text']
        Feedback.objects.create(name=name, mail=mail, text=feedback_text)
        send_mail(
            'Благодарим за отзыв!',
            (f'Здравствуйте, {name}! Спасибо за отзыв о плюшевых черепашках,'
             ' который вы оставили.\n'
             f"{feedback_text}"),
            'from@example.com',
            [f'{mail}'],
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
