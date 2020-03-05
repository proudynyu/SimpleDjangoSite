from django.db import models
from django.utils import timezone

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField('Date', default=timezone.now())

    def __str__(self):
        return self.title