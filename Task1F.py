from re import L
from floodsystem import geo
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    inconsistent_stations = [s.name for s in sorted(inconsistent_typical_range_stations(stations), key=lambda s: s.name)]
    print(inconsistent_stations)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()