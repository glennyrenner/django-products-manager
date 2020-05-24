from django import forms
from .models import *
from .globals import Globals
from dal import autocomplete

class NewDrugForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nom')
    size = forms.IntegerField(label='Boite de')
    dosage = forms.DecimalField(
        max_digits=10, decimal_places=2, label='Dosage')
    dosage_choices = (
        ('g', 'Grammes (g)'),
        ('mg', 'Milligrames (mg)'),
        ('ml', 'Millilitres (ml)')
    )
    dosage_unit = forms.ChoiceField(choices=dosage_choices, label='Unité')

    class Meta:
        model = Drug
        fields = ['name', 'dosage', 'dosage_unit', 'size']


class NewEntryForm(forms.ModelForm):
    drug = forms.ModelChoiceField(queryset=Drug.objects.all(), label='Médicament')
    lot = forms.CharField(max_length=30, label='LOT')
    fab_date = forms.DateField(input_formats=['%d/%m/%Y'], label='Date de fabrication')
    exp_date = forms.DateField(input_formats=['%d/%m/%Y'], label='date d''expiration')
    ppa = forms.DecimalField(max_digits=13, decimal_places=2, label='PPA')
    
    class Meta:
        model = Entry
        fields = '__all__'

class NewSaleForm(forms.Form):
    lot = forms.CharField(max_length=30, label='LOT')
    
    #https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html#create-an-autocomplete-view
    amount = forms.IntegerField(label="Nombre de boites")
