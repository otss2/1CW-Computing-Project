# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine


# Task 1B
def stations_by_distance(stations,p):
    station_name_distance = []
    for i in stations:
        distance = haversine(i.coord,p)
        station_name_distance.append((i, distance))
   
    station_name_distance.sort(key=lambda x: x[1])
    return station_name_distance

# Task 1C
def stations_within_radius(stations, centre, radius):
    x = centre
    stations_in_radius = []
    
    for i in stations:
        distance = haversine(i.coord, x)
        if distance < radius:
            stations_in_radius.append(i)
        if distance == radius:
            stations_in_radius.append(i)
        if distance > radius:
            pass
    return stations_in_radius

# Task 1D
def rivers_with_station(stations):
    out = set()
    for stat in stations:
        #print(stat.river)
        out.add(stat.river)
    return out

def stations_by_river(stations):
    out = {}
    for stat in stations:
        river = stat.river
        if river in out.keys():
            out[river].append(stat)
        else:
            out[river] = [stat]
    return out

# Task 1E
def rivers_by_station_number(stations, N):
    station_rivers = stations_by_river(stations)
    out = []
    for river, stats in station_rivers.items():
        out.append((river, len(stats)))
    out.sort(key=lambda x: x[1], reverse=True)
    cutoff = out[N - 1][1]
    out = [o for o in out if o[1] >= cutoff]
    return out