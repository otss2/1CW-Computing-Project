from .utils import sorted_by_key  # noqa
from .station import MonitoringStation


#Task 2B
def stations_level_over_threshold(stations, tol):
    list = []
    for i in stations:
        if stations.relative_water_level() is None:
            continue
        elif stations.typical_range[1] > stations.typical_range[0]:
            if stations.latest_level > tol:
                list.append(stations.station_id, stations.relative_water_level())
            else:
                continue
        elif stations.typical_range[1] < stations.typical_range[0]:
            continue
    return list
    

#Task 2C
