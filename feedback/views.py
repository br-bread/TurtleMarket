from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import forms


def feedback(request):
    template_name = 'feedback/index.html'
    form = forms.FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        form.cleaned_data['text']
        send_mail(
            'Благодарим за отзыв!',
            ('Здравствуйте! Спасибо за отзыв о плюшевых черепашках,'
             ' который вы оставили.\n'
             f"{form.cleaned_data['text']}"),
            'from@example.com',
            ['to@example.com'],
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
