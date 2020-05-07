from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    adresse = forms.CharField()
    ville = forms.CharField()
    telephone = forms.CharField()
    email = forms.EmailField(label = 'E-mail')
    plainte = forms.ChoiceField(choices= [

    ('conseils', 'Conseils'),
    ('assistance', 'Assistance'),
    ('mediation', 'Médiation'),
    ('reclamation', 'Réclamation'),
    ('plainte', 'Plainte'),
    ('suggestion', 'Suggestion'),
    ('autre', 'Autre'),
    ])
    autre = forms.CharField()
    suggestion = forms.CharField()
    secteur = forms.CharField()
    ministere = forms.ChoiceField(choices= [

    ('Ministère de l\'Economie, du Plan et de la Coopération','Ministère de l\'Economie, du Plan et de la Coopération'),
    ('Ministère des Forces armées','Ministère des Forces armées' ),
    ('Ministère de l\'intérieur', 'Ministère de l\'intérieur'),
    ('Ministère des Finances et du Budget','Ministère des Finances et du Budget'),
    ('Ministère des Affaires étrangères, et des Sénégalais de l\'Extérieur','Ministère des Affaires étrangères, et des Sénégalais de l\'Extérieur'),
    ('Garde des Sceaux, Ministère de la Justice','Garde des Sceaux, Ministère de la Justice'),
    ('Ministère du développement communautaire, de l\'Equité sociale et Territoriale', 'Ministère du développement communautaire, de l\'Equité sociale et Territoriale'),
    ('Ministère du Pétrole et des Energies', 'Ministère du Pétrole et des Energies'),
    ('Ministère de la Fonction publique et Du Renouveau du Service','Ministère de la Fonction publique et Du Renouveau du Service'),
    ('Ministère des Infrastructures, des Transports terrestres et du Désenclavement','Ministère des Infrastructures, des Transports terrestres et du Désenclavement'),
    ('Ministère de la Santé et de l\'Action Sociale', 'Ministère de la Santé et de l\'Action Sociale'),
    ('Ministère de l\'Agriculture et de l\'Equipement Rural','Ministère de l\'Agriculture et de l\'Equipement Rural'),
    ('Ministère de l\'Eau et de l\'Assainissement','Ministère de l\'Eau et de l\'Assainissement'),
    ('Ministère de la Femme, de la Famille, du Genre et de la Protection des Enfants','Ministère de la Femme, de la Famille, du Genre et de la Protection des Enfants'),
    ('Ministère du Tourisme et des Transports aériens','Ministère du Tourisme et des Transports aériens'),
    ('Ministère de l\'Education Nationale','Ministère de l\'Education Nationale'),
    ('Ministère des Collectivités territoriales, du Développement et de l\'Aménagement des Territoires','Ministère des Collectivités territoriales, du Développement et de l\'Aménagement des Territoires'),
    ('Minstère de l\'Enseignement Supérieur, de la Recherche et de l\'Innovation','Minstère de l\'Enseignement Supérieur, de la Recherche et de l\'Innovation'),
    ('Ministère du Développement industriel et des Petites et Moyennes industries','Ministère du Développement industriel et des Petites et Moyennes industries'),
    ('Ministère des Peches et de l\'Economie maritime','Ministère des Peches et de l\'Economie maritime'),
    ('Ministère de l\'Environnement et du Développement Durable','Ministère de l\'Environnement et du Développement Durable'),
    ('Ministère des Mines et de la Géologie','Ministère des Mines et de la Géologie'),
    ('Ministère des Sports','Ministère des Sports'),
    ('Ministère de l\'Elevage et des Productions','Ministère de l\'Elevage et des Productions'),
    ('Ministère du Travail, Dialogue social et des relations avec les Institutions','Ministère du Travail, Dialogue social et des relations avec les Institutions'),
    ('Ministère de l\'Urbanisme , du Logement et l\'Hygiène publique','Ministère de l\'Urbanisme , du Logement et l\'Hygiène publique'),
    ('Ministère du Commerce et des Petites et Moyennes entreprises','Ministère du Commerce et des Petites et Moyennes entreprises'),
    ('Ministère de l\'Economie Numérique et des Télécommunications','Ministère de l\'Economie Numérique et des Télécommunications'),
    ('Ministère de la Microfinance et l’Économie sociale solidaire','Ministère de la Microfinance et l’Économie sociale solidaire'),
    ('Ministère de l’Emploi, de la Formation professionnelle et de l\'Artisanat','Ministère de l’Emploi, de la Formation professionnelle et de l\'Artisanat'),
    ('Ministère de la Culture et de la Communication','Ministère de la Culture et de la Communication'),
    ])

    service = forms.ChoiceField(choices= [

    ('Alimentation', 'Alimentation'),
    ('Commerce et services divers', 'Commerce et services divers'),
    ('Electricité / Gaz / Carburant', 'Electricité / Gaz / Carburant'),
    ('Eau, Assainissement', 'Eau, Assainissement'),
    ('Habitat-Logement / Cadre de vie', 'Habitat-Logement / Cadre de vie'),
    ('Nouvelles technologies de l\'information et de la télécommunication', 'Nouvelles technologies de l\'information et de la télécommunication'),
    ('Santé', 'Santé'),
    ('Transport', 'Transport'),
    ('Banques, assurances, transfert d\'argent', 'Banques, assurances, transfert d\'argent'),
    ])
    message = forms.CharField(widget= forms.Textarea)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
             'prenom': 'Prénom',
             'telephone': 'Téléphone'
        }




    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['suggestion'].required = False
        self.fields['autre'].required = False
        self.fields['plainte'].empty_label = "select"
