from floodsystem import plot
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta

def run():
    """Requirements for Task 2E"""

    # Build list of stations to plot
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    stations_to_plot = stations_highest_rel_level(stations, N)

    # Fetch water level data from those dates
    dt = timedelta(days=10)
    for i in range(len(stations_to_plot)):
        station = stations_to_plot[i]
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)

    



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()




