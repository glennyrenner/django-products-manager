from django.db import models

# Create your models here.
class Drug(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.DecimalField(max_digits=10, decimal_places=2)
    dosage_unit = models.CharField(max_length=5, default='mg')
    size = models.IntegerField(default=30)

    def __str__(self):
        return f'{self.name} {self.dosage}{self.dosage_unit} {self.size}'

    
class Entry(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    lot = models.CharField(max_length=100)
    fab_date = models.DateField()
    exp_date = models.DateField()
    ppa = models.DecimalField(max_digits=15, decimal_places=2)
    number = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.lot}'
