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
    top_stations = stations_highest_rel_level(stations, N)
    stations_to_plot = []
    for s in top_stations:
        stations_to_plot.append(s[0])

    # Build list of station IDs
    ids = []
    for i in stations:
        ids.append()

    
    # Create a list of dates
    t1 = datetime.date.today()
    dtime = timedelta(days=1)
    times = [t1]
    for i in range(1,10):
        times.append(t1 - i*dtime)
    print(times)

    # Fetch water level data from those dates
    dt = 10
    for i in range(stations_to_plot):
        dates, levels = fetch_measure_levels(ids, dt)

    



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()




