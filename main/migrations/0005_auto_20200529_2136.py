# Generated by Django 3.0.3 on 2020-05-29 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200529_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('security_number', models.CharField(default='indéfinie', max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='lot',
            name='ht',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lot',
            name='marge',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lot',
            name='ppa',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lot',
            name='tva',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='indéfinie', max_length=20)),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
    ]
