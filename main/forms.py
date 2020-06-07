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

