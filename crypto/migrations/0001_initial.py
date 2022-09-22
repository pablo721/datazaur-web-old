# Generated by Django 4.1 on 2022-09-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('macro', '0001_initial'),
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('symbol', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('hash_algorithm', models.CharField(blank=True, max_length=64, null=True)),
                ('proof_type', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=32)),
                ('is_quote_fiat', models.BooleanField(blank=True, null=True)),
                ('bid', models.FloatField(blank=True, null=True)),
                ('ask', models.FloatField(blank=True, null=True)),
                ('source', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto.cryptocurrency')),
            ],
        ),
        migrations.CreateModel(
            name='CryptoExchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('grade', models.CharField(blank=True, choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'NA')], max_length=3, null=True)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('daily_vol', models.FloatField(blank=True, null=True)),
                ('monthly_vol', models.FloatField(blank=True, null=True)),
                ('countries', models.ManyToManyField(related_name='cryptoexchange_countries', to='macro.country')),
                ('currencies', models.ManyToManyField(related_name='cryptoexchange_currencies', to='markets.currency')),
                ('tickers', models.ManyToManyField(related_name='cryptoexchange_tickers', to='markets.ticker')),
            ],
        ),
    ]
