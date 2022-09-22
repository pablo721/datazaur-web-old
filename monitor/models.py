from django.db import models


class Watchlist(models.Model):
    creator = models.ForeignKey('website.Account', related_name='watchlist_creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default='Watchlist')
    currency = models.ForeignKey('markets.Currency', on_delete=models.CASCADE, related_name='watchlist_currency',
                                 blank=True, null=True)
    tickers = models.ManyToManyField('markets.Ticker', related_name='watchlist_tickers', blank=True)

#
# class Portfolio(Watchlist):
#     amounts = models.ManyToManyField('markets.Asset', related_name='portfolio_assets', blank=True,
#                                    through='watchlist.Amounts', through_fields=('portfolio', 'asset', 'amount', 'asset_class'))
#
#
#
# class Amounts(models.Model):
#     portfolio = models.OneToOneField('watchlist.Portfolio', on_delete=models.CASCADE, related_name='portfolio_crypto_amount')
#     asset = models.ForeignKey('markets.Asset', related_name='amounts_asset', blank=True, on_delete=models.CASCADE)
#     asset_class = models.CharField(max_length=32)
#     amount = models.FloatField(default=0)
#


