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
    """Requirements for Task 2G"""

    # Build list of stations to plot
    stations = build_station_list()
    update_water_levels(stations)
    dt = timedelta(days=2)
    counts = {"Severe": 0, "High": 0, "Moderate": 0, "Low": 0, "No data": 0}
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if levels and station.typical_range is not None:
            poly, d0 = polyfit(dates, levels, 4)
            x = matplotlib.dates.date2num(dates)
            x -= d0
            pred = poly(x)
            pred_time = 1#day
            pred_time = pred_time * 24 * 60 #minutes
            #dates every 15 mins
            pred_level = levels[-1] + (pred[0] - pred[1]) * (pred_time / 15)
            pred_date = dates[0] + (pred_time / 15) * timedelta(minutes=15)
            x1 = matplotlib.dates.date2num([pred_date]) - d0
            pred_level_2 = poly(x1)[0]  

            plt.plot(dates, levels)
            plt.plot(dates, pred)
            plt.axhline(y=station.typical_range[0], ls="--")
            plt.axhline(y=station.typical_range[1], ls="--")

            plt.plot(pred_date, pred_level, "r+")
            plt.plot(pred_date, pred_level_2, "g+")

            #plt.show()

            if pred_level > station.typical_range[1] * 1.5:
                print(f"{station.name}: Severe")
                counts["Severe"] += 1
            elif pred_level > station.typical_range[1] * 1.2:
                print(f"{station.name}: High")
                counts["High"] += 1
            elif pred_level > station.typical_range[1] * 1:
                print(f"{station.name}: Moderate")
                counts["Moderate"] += 1
            else:
                print(f"{station.name}: Low")
                counts["Low"] += 1
        else:
            print(f"{station.name}: No data")
            counts["No data"] += 1
    
    print()
    print("Summary:")
    for state in counts.keys():
        print(f"{state} - {counts[state]}")
    



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()




