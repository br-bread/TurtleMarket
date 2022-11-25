from django.db import models


class Feedback(models.Model):
    name = models.CharField('имя пользователя',
                            max_length=100,
                            help_text='Максимальная длина 100 символов')
    mail = models.EmailField('почта',
                             max_length=150,
                             blank=False,
                             default='mail@mail.com')
    text = models.CharField('отзыв',
                            max_length=300,
                            help_text='Максимальная длина 300 символов',
                            blank=False)

    created_on = models.DateTimeField('дата создания',
                                      auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.text[:20]
