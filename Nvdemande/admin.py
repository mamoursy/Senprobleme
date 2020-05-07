from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','prenom','nom','adresse','plainte')
    list_display_links = ('id', 'prenom')
    list_filter = ('plainte',)
    search_fields = ('adresse', 'ville', 'secteur', 'plainte')
    list_per_page = 25





admin.site.register(Contact, ContactAdmin)
