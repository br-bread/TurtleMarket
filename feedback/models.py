from django.db import models


class Feedback(models.Model):
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
