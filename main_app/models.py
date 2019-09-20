from django.db import models
from django.urls import reverse


class Wish(models.Model):
    description=models.TextField(max_length=400)
    quantity=models.IntegerField()

    def get_absolute_url(self):
        return reverse('index', kwargs={'wish_id': self.id})

