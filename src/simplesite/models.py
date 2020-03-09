from django.db import models
from django.utils import timezone

class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    tut_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.series

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField('Date', default=timezone.now())
    tut_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)

    tutorial_slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title