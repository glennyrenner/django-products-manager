from django.db import models
import datetime
# Create your models here.


class Drug(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    size = models.IntegerField(default=30)

    def __str__(self):
        return f'{self.name} {self.dosage}{self.size}'


class Entry(models.Model):
    number = models.CharField(max_length=30, default='-------')
    bill_number = models.CharField(max_length=30, default='-------')
    date = models.DateField()

    def __str__(self):
        return '{}'.format(self.number)


class Lot(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, default='')
    lot_number = models.CharField(max_length=30)
    exp_date = models.DateField()
    qte = models.IntegerField()
    tva = models.CharField(max_length=30)
    ht = models.CharField(max_length=30)
    ppa = models.CharField(max_length=30)
    marge = models.CharField(max_length=30)

    def __str__(self):
        return '{} LOT:{} {}'.format(self.drug.name, self.lot_number, self.exp_date)


class Client(models.Model):
    first_name = models.CharField(max_length=30, default='indéfinie')
    last_name = models.CharField(max_length=30, default='indéfinie')
    security_number = models.CharField(max_length=40, default='indéfinie')

    def __str__(self):
        return '{} {} {}'.format(self.first_name,
                                 self.last_name, str(self.security_number)[:2])


class Prescription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default='indéfinie')
    date = models.DateField(default=datetime.date.today)
    prods = models.CharField(max_length=1024, default='indéfinie')

    def __str__(self):
        return '{}'.format(self.number)

