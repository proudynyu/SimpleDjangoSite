from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'date']

admin.site.register(Tutorial, TutorialAdmin)