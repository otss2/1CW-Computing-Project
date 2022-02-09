# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.geo import *
from floodsystem.station import MonitoringStation

def get_test_stations():
    s1 = MonitoringStation("a", "1", "x", (13, 0), (2, 1), "r1", "t1") #inconsistent range
    s2 = MonitoringStation("b", "2", "y", (1, 11), (3, 4), "r1", "t2")
    s3 = MonitoringStation("c", "3", "z", (1, 10), (3, 2), "r3", "t3") #inconsistent range
    s4 = MonitoringStation("d", "4", "w", (13, 26), (0, 0), "r4", "t4") #inconsistent range
    s5 = MonitoringStation("e", "5", "v", (20, 30), None, "r3", "t5") #inconsistent range
    test_stations = [s1, s2, s3, s4, s5]

    return test_stations

def test_stations_by_distance():
    test_stats = get_test_stations()
    assert [x[0] for x in stations_by_distance(test_stats,(0, 10))] == [test_stats[2], test_stats[1], test_stats[0], test_stats[3], test_stats[4]]

def test_stations_within_radius():
    test_stats = get_test_stations()
    out = stations_within_radius(test_stats, (0, 10), 300)
    assert out == [test_stats[1], test_stats[2]]

def test_rivers_with_station():
    test_stats = get_test_stations()
    out = rivers_with_station(test_stats)
    assert out == set(["r1", "r3", "r4"])

def test_stations_by_river():
    test_stats = get_test_stations()
    out = stations_by_river(test_stats)
    assert out == {"r1": [test_stats[0], test_stats[1]], "r3": [test_stats[2], test_stats[4]], "r4": [test_stats[3]]}

def test_rivers_by_station_number():
    test_stats = get_test_stations()
    out = [r for r,n in rivers_by_station_number(test_stats, 2)]
    out2 = [r for r,n in rivers_by_station_number(test_stats, 1)]
    assert out == out2 and out == ["r1", "r3"]