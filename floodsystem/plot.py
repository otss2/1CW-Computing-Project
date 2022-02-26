from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Task 2E
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()