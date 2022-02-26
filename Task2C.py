from floodsystem import flood
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    N = 10
    list = stations_highest_rel_level(stations, N)
    for s in list:
        print(s[0], s[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()