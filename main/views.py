from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib import messages
from .globals import Globals
import json
import time
# Create your views here.

import datetime
import calendar


def add_months(sourcedate, months):
    # NOT A VIEW
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def home(request):
    lots = Lot.objects.all()
    articles = 0
    close_exps = 0

    # make this customizable later
    warning_date = add_months(datetime.date.today(), 6)

    for lot in lots:
        articles += lot.qte

        wd = '{}'.format(warning_date).replace('-', '')
        ed = '{}'.format(lot.exp_date).replace('-', '')
        td = '{}'.format(datetime.date.today()).replace('-', '')

        if int(ed) < int(wd) and int(ed) > int(td):
            close_exps += 1

    context = {
        'close_exps': close_exps,
        'clients': len(Client.objects.all()),
        'articles': articles,
        'sales': len(Prescription.objects.all()),
    }
    return render(request, 'main/home.html', context)


def get_drugs_list(request):
    all_drugs = Drug.objects.all()
    drugs = []
    for d in all_drugs:
        lots = Lot.objects.filter(
            drug__name=d.name, drug__dosage=d.dosage, drug__size=d.size)
        if lots.exists():
            qtt = 0
            for lot in lots:
                qtt += lot.qte
            drugs.append({
                'name': d.name,
                'dosage': d.dosage,
                'size': d.size,
                'qtt': qtt
            })
    resp = {
        'drugs': drugs
    }
    return JsonResponse(resp)


def request_entries(request):
    drug_id = request.GET.get('drug_id')
    Globals.selected_id = drug_id
    drug_name = Drug.objects.filter(id=drug_id).first().name
    entries = Entry.objects.filter(drug__id=drug_id).values()
    return JsonResponse({'entries': list(entries),
                         'selected': drug_name,
                         })


def add_entry(request):
    return render(request, 'main/add_entry.html')


def add_drug(request):
    form = NewDrugForm()
    return render(request, 'main/add_drug.html', {'form': form})


def add_sale(request):
    # hand over drugs
    # each with it's available dosages and lots
    drugs = Drug.objects.all()
    context = {
        'drugs': drugs
    }
    return render(request, 'main/add_sale.html', context)


def save_sale(request):
    presc = json.loads(request.POST.get('presc'))
    client, created = Client.objects.get_or_create(
        first_name=presc['f_name'],
        last_name=presc['l_name'],
        security_number=presc['sec_num']
    )
    try:
        new = Prescription(
            client=client,
            number=int(time.time()*10)
        )

        prods_str = ''
        for p in presc['prods']:
            prods_str += '{} {} {} {} | '.format(
                p['name'],
                p['dosage'],
                p['qtt'],
                p['lot'],
            )
            prod = Lot.objects.filter(lot_number=p['lot'],
                                      drug__name=p['name']).first()

            prod.qte -= int(p['qtt'])
            prod.save()

        new.prods = prods_str
        new.save()
        message = 'Vente enregistrée avec succès!'
        tag = 'alert-success'
    except Exception as e:
        print("Oh shit Morty! {}".format(e))
        message = "Une erreur s'est produite"
        tag = 'alert-danger'

    return JsonResponse({
        'message': message,
        'tag': tag
    })


def save_entry(request):
    try:
        num = request.POST.get('num')
        bill = request.POST.get('bill')
        date = request.POST.get('date')
        prods = json.loads(request.POST.get('prods'))

        fdate = '{}-{}-{}'.format(
            date.split('/')[2],
            date.split('/')[1],
            date.split('/')[0],
        )
        # add a drug if it doesn't exist with the given name
        entry = Entry(
            number=num,
            bill_number=bill,
            date=fdate
        )
        entry.save()

        for prod in prods:
            d = prod['exp'].split('/')
            nd = '{}-{}-{}'.format(d[2], d[1], d[0])
            lot = Lot(
                entry=entry,
                lot_number=prod['lot'],
                exp_date=nd,
                qte=prod['qtt'],
                tva=prod['tva'],
                ht=prod['ht'],
                ppa=prod['ppa'],
                marge=prod['marge']
            )
            # already have these or new shit?
            existing = Drug.objects.filter(name=prod['name'],
                                           dosage=prod['dosage'],
                                           size=prod['size'])
            if existing:
                lot.drug = existing.first()
            else:
                drug = Drug(name=prod['name'],
                            dosage=prod['dosage'],
                            size=prod['size'])
                drug.save()
                lot.drug = drug
            lot.save()

        return JsonResponse({
            'message': 'Entrée ajoutée avec succès',
            'tag': 'alert-success'
        })
    except Exception as e:
        print("Oh shit, Morty {}".format(e))
        return JsonResponse({
            'tag': 'alert-danger',
            'message': "Oups, un problème est survenu, les données nont pas été enregistrées."})


def get_drug_details(request):
    lots = Lot.objects.filter(
        drug__name=request.GET.get('name'),
        drug__dosage=request.GET.get('dosage'),
        drug__size=request.GET.get('size')
    )

    resp = []
    for l in lots:
        resp.append({
            'number': l.lot_number,
            'exp_date': l.exp_date,
            'qte': l.qte,
            'tva': l.tva,
            'ht': l.ht,
            'ppa': l.ppa,
            'marge': l.marge,
            'entry': l.entry.number
        })

    full_name = '{} {} B/{}'.format(
        request.GET.get('name'),
        request.GET.get('dosage'),
        request.GET.get('size')
    )
    return JsonResponse({
        'name': full_name,
        'lots': resp
    })


def get_prod_info(request):
    # in case future me wonders, difference between this an dthe one above is this gives on lot
    # the other gives details on all lots of that product.
    prod = Lot.objects.filter(lot_number=request.GET.get('lot'),
                              drug__name=request.GET.get('name'),
                              drug__dosage=request.GET.get('dosage'),
                              drug__size=request.GET.get('size'),
                              ).first()
    # no product at all?
    if not prod:
        return JsonResponse(
            data={
                'status': False,
                'msg': 'Produit non trouvé'
            },
        )

    # do we have enough items?
    if prod.qte < int(request.GET.get('qtt')):
        return JsonResponse(
            data={
                'status': False,
                'msg': "La quantité en stock n'est pas suffisante"
            },
        )

    # in case it's found
    return JsonResponse({
        'status': True,
        'msg': 'Added succesfully',
        'ppa': prod.ppa,
        'exp_date': prod.exp_date
    })
