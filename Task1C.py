from floodsystem import geo
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations within certain radius of specified point
    stations_in_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)

    print(sorted([s.name for s in stations_in_radius]))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()