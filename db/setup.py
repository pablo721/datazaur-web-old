import datetime
import time
import pandas as pd
from .db import load_config
from .load_calendars import load_all_calendars
from .load_countries import load_currencies, map_currencies
from .load_pd import wb_countries, wb_sources, wb_regions, wb_lendingtypes, wb_incomelevels, wb_topics, wb_indicators
from .load_stocks import load_exchanges, load_stocks_finnhub
from .pipelines import pipeline_wb2, pipeline_wb



setup_funcs2 = [wb_countries, wb_sources, wb_regions, wb_lendingtypes, wb_incomelevels, load_currencies, map_currencies,
                load_all_calendars, load_exchanges, load_stocks_finnhub]


def setup_all():
    success = []
    errors = []
    for func in setup_funcs2:
        try:
            t = datetime.datetime.now().timestamp()
            print(f'Starting {func.__name__}')
            func()
            print(f'Function {func.__name__} executed successfully in {datetime.datetime.now().timestamp() - t} seconds.')
            success.append(func.__name__)
        except Exception as e:
            print(f'Error {e} while executing function {func.__name__}.')
            errors.append([func.__name__, e])
        finally:
            time.sleep(1)

    print(f'Successes: {success} \nFailures: {errors}')
    return success, errors


