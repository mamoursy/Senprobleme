from django.contrib import admin
from .models import traitement

# Register your models here.

class TraitementAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'statut')
    list_display_links = ('id', 'contact', 'statut')
    search_fields = ('contact',)
#    list_editable = ('STATUT',)
    list_per_page = 25



admin.site.register(traitement, TraitementAdmin)
