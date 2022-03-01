from floodsystem import plot
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
from floodsystem.analysis import *

def run():
    """Requirements for Task 2F"""

    # Build list of stations to plot
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    stations_to_plot = stations_highest_rel_level(stations, N)
    dt = timedelta(days=2)
    for station in stations_to_plot:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if levels:
            plot_water_level_with_fit(station, dates, levels, 4)
    



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()




