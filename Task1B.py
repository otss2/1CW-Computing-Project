from floodsystem import geo
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""
    
    # Build list of stations
    stations = build_station_list()

    # Build list of stations and distances from coordinate
    station_name_distance = geo.stations_by_distance(stations, (52.2053,0.1218))

    for s, d in station_name_distance[:10]:
        print(s.name, s.town, d)

    print()

    for s, d in station_name_distance[-10:]:
        print(s.name, s.town, d)





if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()


#geo.stations_by_distance(build_station_list(), (52.2053,0.1218))
#print(stations_by_distance(build_station_list(),(52.2053,0.1218)))