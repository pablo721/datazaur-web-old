from django.db import models
from config import constants



class Asset(models.Model):
    ASSET_CLASSES = ['cryptocurrency', 'currency', 'commodity', 'equity', 'bond', 'real estate', 'fund share', 'na']
    name = models.CharField(max_length=64, null=True, blank=True)
    symbol = models.CharField(max_length=32, primary_key=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    asset_class = models.CharField(max_length=16, choices=enumerate(ASSET_CLASSES), default='na')

    class Meta:
        abstract = True


class Currency(Asset):
    issuer_id = models.CharField(max_length=2)



class Commodity(Asset):
    COMMODITY_GROUPS = ['metals', 'softs', 'meats', 'energy', 'grains', 'na']
    group = models.CharField(max_length=21, choices=enumerate(COMMODITY_GROUPS), null=True, blank=True)




class Ticker(models.Model):
    base = models.CharField(max_length=32)
    quote = models.CharField(max_length=32)
    bid = models.FloatField(blank=True, null=True)
    ask = models.FloatField(blank=True, null=True)
    source = models.CharField(max_length=128)
    timestamp = models.DateTimeField(blank=True, null=True)



class Index(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=64, primary_key=True)
    country_id = models.CharField(max_length=2)
    currency_code = models.CharField(max_length=3)
    index_type = models.CharField(max_length=32, default='na')
    value = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)



class Exchange(models.Model):
    code = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=64)
    mic = models.CharField(max_length=64)
    timezone = models.CharField(max_length=64)
    hours = models.CharField(max_length=64)
    country_code = models.CharField(max_length=8)
    source = models.CharField(max_length=128)


class Security(models.Model):
    symbol = models.CharField(max_length=16)
    name = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchange = models.CharField(max_length=64, blank=True, null=True)
    exchangeShortName = models.ForeignKey('markets.Exchange', on_delete=models.CASCADE, related_name='security_exchange')
    type = models.CharField(max_length=32)


class Stock(models.Model):
    currency_id = models.CharField(max_length=3, null=True, blank=True)
    exchange = models.ForeignKey('markets.Exchange', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    displaySymbol = models.CharField(max_length=16, null=True, blank=True)
    figi = models.CharField(max_length=12, null=True, blank=True)
    isin = models.CharField(max_length=12, null=True, blank=True)
    mic = models.CharField(max_length=16, null=True, blank=True)
    shareClassFIGI = models.CharField(max_length=16, null=True, blank=True)
    symbol = models.CharField(max_length=16, null=True, blank=True)
    symbol2 = models.CharField(max_length=16, null=True, blank=True)
    stock_class = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=32)



class Bond(models.Model):
    country_id = models.CharField(max_length=2)
    name = models.CharField(max_length=32)
    last = models.FloatField()
    last_close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    change = models.FloatField()
    change_percentage = models.FloatField()

