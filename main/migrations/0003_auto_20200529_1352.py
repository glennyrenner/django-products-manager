# Generated by Django 3.0.3 on 2020-05-29 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_entry_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='dosage_unit',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='drug',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='fab_date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='ppa',
        ),
        migrations.AddField(
            model_name='entry',
            name='bill_number',
            field=models.CharField(default='-------', max_length=30),
        ),
        migrations.AlterField(
            model_name='drug',
            name='dosage',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='entry',
            name='number',
            field=models.CharField(default='-------', max_length=30),
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_number', models.CharField(max_length=30)),
                ('exp_date', models.DateField()),
                ('qte', models.IntegerField()),
                ('tva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ht', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ppa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('marge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Entry')),
            ],
        ),
    ]