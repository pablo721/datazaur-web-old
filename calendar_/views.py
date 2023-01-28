from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.dateparse import parse_datetime
import investpy
from .models import MacroCalendar, CryptoCalendar, IPOCalendar, EarningsCalendar


class MacroCalendarView(TemplateView):
    template_name = 'calendar_/macro_calendar.html'

    def get_context_data(self, **kwargs):
        return {'calendar': MacroCalendar.objects.all(),
                'columns': [f.name for f in MacroCalendar._meta.get_fields()]}


class CryptoCalendarView(TemplateView):
    template_name = 'calendar_/crypto_calendar.html'

    def get_context_data(self, **kwargs):
        calendar = CryptoCalendar.objects.all()
        for event in calendar:
             event.date_event = parse_datetime(event.date_event.strftime("%Y:%M:%D"))

        return {'calendar': calendar,
                'columns': [f.name for f in CryptoCalendar._meta.get_fields()]}


class IPOCalendarView(TemplateView):
    template_name = 'calendar_/ipo_calendar.html'

    def get_context_data(self, **kwargs):
        return {'calendar': IPOCalendar.objects.all(),
                'columns': [f.name for f in IPOCalendar._meta.get_fields()]}


class EarningsCalendarView(TemplateView):
    template_name = 'calendar_/earnings_calendar.html'

    def get_context_data(self, **kwargs):
        return {'calendar': EarningsCalendar.objects.all(),
                'columns': [f.name for f in EarningsCalendar._meta.get_fields()]}
