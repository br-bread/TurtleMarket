from django.db import models


class Feedback(models.Model):
    text = models.CharField(max_length=300, help_text='Отзыв о товаре')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
