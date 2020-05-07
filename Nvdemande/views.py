from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            adresse = form.cleaned_data['adresse']
            ville = form.cleaned_data['ville']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            plainte = form.cleaned_data['plainte']
            suggestion = form.cleaned_data['suggestion']
            autre = form.cleaned_data['autre']
            secteur = form.cleaned_data['secteur']
            ministere = form.cleaned_data['ministere']
            service = form.cleaned_data['service']
            message = form.cleaned_data['message']
            form.save()
            send_mail(
                'SENPROBLEME confirmation',
                'Bonjour Mr. ' + nom + ' votre plainte a étè bien reçu',
                'mamoursy@gmail.com',
                [email,'mamoursy@gmail.com', 'amdieye@gmail.com'],
                fail_silently=False
            )
            return redirect('envoyer-avec-success/')

            # send an email



#            print(nom, prenom, adresse, ville, telephone, email, plainte,
#            suggestion, autre, secteur, ministere, service, message)

    form = ContactForm()
    return render (request, 'Nouvelle demande/Ndemande.html', {'form': form })




def suivi(request):
    return render (request, 'Nouvelle demande/suivi.html')

def statistiques(request):
    return render (request, 'Nouvelle demande/statistiques.html')


def confirmation(request):
    return render (request, 'Nouvelle demande/envoyer-avec-success.html')
