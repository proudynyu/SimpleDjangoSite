from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'fields' : ['title', 'date']}),
        ('Description', {'fields': ['description']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin)