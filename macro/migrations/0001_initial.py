# Generated by Django 4.1.3 on 2022-12-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso3c', models.CharField(max_length=3)),
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('region', models.CharField(blank=True, max_length=64, null=True)),
                ('adminregion', models.CharField(blank=True, max_length=64, null=True)),
                ('incomeLevel', models.CharField(blank=True, max_length=64, null=True)),
                ('lendingType', models.CharField(blank=True, max_length=64, null=True)),
                ('capitalCity', models.CharField(max_length=128)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('currency_code', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('iso2code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='WBIncomeLevel',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('iso2code', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='WBLendingType',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('iso2code', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='WBSource',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('lastupdated', models.DateTimeField()),
                ('name', models.CharField(max_length=70)),
                ('code', models.CharField(max_length=3)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WBTopic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=70)),
                ('sourceNote', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='WBIndicator',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('unit', models.CharField(blank=True, max_length=16, null=True)),
                ('source', models.CharField(blank=True, max_length=128, null=True)),
                ('sourceNote', models.CharField(max_length=512)),
                ('sourceOrganization', models.CharField(max_length=256)),
                ('topics', models.ManyToManyField(to='macro.wbtopic')),
            ],
        ),
    ]
