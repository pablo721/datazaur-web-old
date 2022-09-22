from django.db import models
from config import constants


class CryptoExchange(models.Model):
    name = models.CharField(max_length=128)
    grade = models.CharField(choices=enumerate(constants.CRYPTO_EXCHANGE_GRADES), max_length=3, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    countries = models.ManyToManyField('macro.Country', related_name='cryptoexchange_countries')
    currencies = models.ManyToManyField('markets.Currency', related_name='cryptoexchange_currencies')
    tickers = models.ManyToManyField('markets.Ticker', related_name='cryptoexchange_tickers')
    daily_vol = models.FloatField(null=True, blank=True)
    monthly_vol = models.FloatField(null=True, blank=True)


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    symbol = models.CharField(max_length=64, primary_key=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    hash_algorithm = models.CharField(max_length=64, null=True, blank=True)
    proof_type = models.CharField(max_length=32, null=True, blank=True)


class CryptoQuote(models.Model):
    base = models.ForeignKey('crypto.Cryptocurrency', on_delete=models.CASCADE)
    quote = models.CharField(max_length=32)
    is_quote_fiat = models.BooleanField(null=True, blank=True)
    bid = models.FloatField(blank=True, null=True)
    ask = models.FloatField(blank=True, null=True)
    source = models.CharField(max_length=128)
    timestamp = models.DateTimeField(blank=True, null=True)



