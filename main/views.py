from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib import messages
from .globals import Globals
from dal import autocomplete
# Create your views here.


def home(request):
    # check if POST
    if request.method == "POST":
        if 'new_drug' in request.POST:
            form = NewDrugForm(request.POST)
            print('new durg')
        elif 'new_entry' in request.POST:
            print('new entry')
            form = NewEntryForm(request.POST)
        elif 'new_sale' in request.POST:
            print('new sale')
            form = NewSaleForm(request.POST)
            if form.is_valid():
                entry = Entry.objects.filter(
                    lot=form.cleaned_data['lot']).first()
                number = form.cleaned_data['amount']
                if number > entry.number:
                    messages.error(
                        request, "Le numéro d'article n'est pas suffisant")
                    return redirect('home')
                else:
                    entry.number -= int(number)
                    entry.save()
                    messages.success(request, "Destockage avec succès")
                    return redirect('home')
            else:
                messages.error(
                    request, 'Veuillez vérifier le formulaire et soumettre à nouveau')
                return redirect('home')

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Enregistré avec succès un nouveau médicament')
            return redirect('home')
        else:
            messages.error(
                request, 'Veuillez vérifier le formulaire et soumettre à nouveau')
            return redirect('home')

    drugs = Drug.objects.all()
    drug_form = NewDrugForm()
    entry_form = NewEntryForm()
    sale_form = NewSaleForm()

    new_drugs = []
    for drug in drugs:
        new_drug = {}
        if str(drug.dosage)[-2:] == '00':
            new_drug['dosage'] = str(drug.dosage)[:-3]
        else:
            new_drug['dosage'] = str(drug.dosage)
        new_drug['name'] = drug.name
        new_drug['dosage_unit'] = drug.dosage_unit
        new_drug['size'] = drug.size
        new_drug['id'] = drug.id
        new_drugs.append(new_drug)

    context = {
        'drugs': new_drugs,
        'new_drug_form': drug_form,
        'new_entry_form': entry_form,
        'new_sale_form': sale_form,

    }
    return render(request, 'main/home.html', context)


def request_entries(request):
    drug_id = request.GET.get('drug_id')
    Globals.selected_id = drug_id
    drug_name = Drug.objects.filter(id=drug_id).first().name
    entries = Entry.objects.filter(drug__id=drug_id).values()
    return JsonResponse({'entries': list(entries),
                         'selected': drug_name,
                         })


class LOTAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        l = ['fuck', 'you']
        return l
