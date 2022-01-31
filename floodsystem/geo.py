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
    station_name_distance = {}
    for i in stations:
        distance = haversine(stations.coord,p)
        station_name_distance.append(stations.station_id, distance)
   
    sorted_by_key(station_name_distance,1)
    return station_name_distance

# Task 1C
def stations_within_radius(stations, centre, radius):
    x = centre
    stations_in_radius = []
    
    for i in stations:
        distance = haversine(stations.coord, x)
        if distance < radius:
            stations_in_radius.append(stations.station_id)
        if distance == radius:
            stations_in_radius.append(stations.station_id)
        if distance > radius:
            continue
    return stations_in_radius




