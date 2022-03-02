from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import *

#Task 2E
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.axhline(y=station.typical_range[0], ls="--")
    plt.axhline(y=station.typical_range[1], ls="--")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)

    plt.plot(dates, levels)
    x = matplotlib.dates.date2num(dates)
    x -= d0
    pred = poly(x)
    plt.plot(dates, pred)
    plt.axhline(y=station.typical_range[0], ls="--")
    plt.axhline(y=station.typical_range[1], ls="--")
    plt.show()