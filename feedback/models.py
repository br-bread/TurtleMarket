from django.db import models


class Feedback(models.Model):
    text = models.CharField(max_length=300,
                            help_text='Максимальная длина 300 символов')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
