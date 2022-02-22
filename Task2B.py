from floodsystem import flood
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    tol = 0.8
    list = stations_level_over_threshold(stations, tol)
    for s in list:
        print(s[0], s[1])

    # over_threshold = flood.stations_level_over_threshold(stations, 0.8)
    
    # print(over_threshold)

    # for station in stations:
    #     print(station.station_id, station.latest_level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()