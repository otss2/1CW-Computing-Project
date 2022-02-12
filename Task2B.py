from floodsystem import flood
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()

    over_threshold = flood.stations_level_over_threshold(stations, 0.8)
    
    print(over_threshold)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()