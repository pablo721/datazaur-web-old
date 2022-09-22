

from rest_framework import serializers
from markets.models import Ticker, Asset, Commodity, Currency
from macro.models import Country
from crypto.models import CryptoExchange, Cryptocurrency
from monitor.models import *
from calendar_.models import MacroCalendar, CryptoCalendar




class TickerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticker
		fields = ['asset_class', 'base', 'base_full_name', 'quote', 'quote_full_name']


class AssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ['name', 'symbol', 'asset_class']


class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ['name', 'code', 'issuer']


class CurrencySerializer(serializers.ModelSerializer):
	class Meta:
		model = Currency
		fields = ['code', 'name', 'countries']


class CommoditySerializer(serializers.ModelSerializer):
	class Meta:
		model = Commodity
		fields = ['name', 'symbol', 'group']


class CryptoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cryptocurrency
		fields = ['url']


class CryptoExchangeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CryptoExchange
		fields = ['symbol', 'name', 'url']


class WatchlistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Watchlist
		fields = ['name', 'creator', 'tickers']


# class PortfolioSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Portfolio
# 		fields = ['name', 'creator', 'currency', 'assets', 'private', 'creation_date']



class MacroCalendarSerializer(serializers.ModelSerializer):
	class Meta:
		model = MacroCalendar
		fields = ['name']


class CryptoCalendarSerializer(serializers.ModelSerializer):
	class Meta:
		model = CryptoCalendar
		fields = ['name']


