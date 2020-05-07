from django.db import models
from Nvdemande.models import Contact



STATUT = (
    ('En cours', 'En cours'),
    ('Traité', 'Traité'),
    ('Cloturé', 'Cloturé'),
    ('Sans Objet', 'Sans Objet'),
    )



class traitement(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    statut = models.CharField(max_length=120, default='En cours', choices= STATUT)

    def __str__ (self):
       return self.contact
