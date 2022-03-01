from .utils import sorted_by_key  # noqa
from .station import MonitoringStation


#Task 2B
def stations_level_over_threshold(stations, tol):
    list = []
    for station in stations:
        if station.relative_water_level() is None:
            continue
        elif station.typical_range[1] > station.typical_range[0]:
            if station.relative_water_level() > tol:
                list.append((station, station.relative_water_level()))
            else: 
                continue
        elif station.typical_range[1] < station.typical_range[0]:
            continue
    list = sorted(list, key=lambda x: x[1], reverse=True)
    return list
    

#Task 2C
def stations_highest_rel_level(stations, N):
    mylist = []
    for station in stations:
        if station.relative_water_level() is None:
            continue
        elif station.typical_range[1] < station.typical_range[0]:
            continue
        elif station.typical_range[1] > station.typical_range[0]:
            mylist.append((station, station.relative_water_level()))
    mylist = sorted(mylist, key=lambda x: x[1], reverse=True)[:N]
    mylist = [x[0] for x in mylist]
    return mylist



