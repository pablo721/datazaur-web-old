from django.http import JsonResponse
import django_filters.rest_framework as rest_filters
from rest_framework import viewsets
from .serializers import *
from markets.models import Ticker, Currency, Commodity, Asset
from crypto.models import Cryptocurrency
from macro.models import Country
from monitor.models import *
from calendar_.models import MacroCalendar, CryptoCalendar



class TickerView(viewsets.ModelViewSet):
	queryset = Ticker.objects.all()
	serializer_class = TickerSerializer
	filter_backends = [rest_filters.DjangoFilterBackend]






class CryptoView(viewsets.ModelViewSet):
	queryset = Cryptocurrency.objects.all()
	serializer_class = CryptoSerializer
	filter_backends = [rest_filters.DjangoFilterBackend]

	def get_queryset(self):
		return JsonResponse({'a': 1})


class WatchlistView(viewsets.ModelViewSet):
	queryset = Watchlist.objects.all()
	serializer_class = WatchlistSerializer


# class PortfolioView(viewsets.ModelViewSet):
# 	queryset = Portfolio.objects.all()
# 	serializer_class = PortfolioSerializer


class CurrencyView(viewsets.ModelViewSet):
	queryset = Currency.objects.all()
	serializer_class = CurrencySerializer


class CountryView(viewsets.ModelViewSet):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer


class CommodityView(viewsets.ModelViewSet):
	queryset = Commodity.objects.all()
	serializer_class = CommoditySerializer


class MacroCalendarView(viewsets.ModelViewSet):
	queryset = MacroCalendar.objects.all()
	serializer_class = MacroCalendarSerializer


class CryptoCalendarView(viewsets.ModelViewSet):
	queryset = CryptoCalendar.objects.all()
	serializer_class = CryptoCalendarSerializer



