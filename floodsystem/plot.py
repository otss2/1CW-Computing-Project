from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Task 2E
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)