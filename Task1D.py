from floodsystem import geo
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    new_stations = rivers_with_station(stations)

    print(len(new_stations))

    print(sorted(list(new_stations))[:10])

    river_stations = stations_by_river(stations)

    for river in ["River Aire", "River Cam", "River Thames"]:
        print(river)
        print(sorted([s.name for s in river_stations[river]]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()