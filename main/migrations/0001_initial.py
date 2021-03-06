# Generated by Django 3.0.3 on 2020-05-19 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dosage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dosage_unit', models.CharField(default='mg', max_length=5)),
                ('size', models.IntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=100)),
                ('fab_date', models.DateField()),
                ('exp_date', models.DateField()),
                ('ppa', models.DecimalField(decimal_places=2, max_digits=15)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Drug')),
            ],
        ),
    ]
