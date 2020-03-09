from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial, TutorialSeries, TutorialCategory

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'fields' : ['title', 'date']}),
        ('URL', {'fields' : ['tutorial_slug']}),
        ('Series', {'fields' : ['tut_series']}),
        ('Content', {'fields': ['description']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)